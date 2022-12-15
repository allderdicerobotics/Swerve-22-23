import math
import typing as t

from magicbot import magiccomponent
from components.swervemodule import SwerveModule

from wpimath import kinematics

import wpilib
import rev
import attrs

import components.component_constants as c

T = t.TypeVar("T")
PerModule = t.Dict[t.Literal["FL", "FR", "BL", "BR"], T]

SWERVE_MODULE_TAGS = ("FL", "FR", "BL", "BR")

@attrs.define
class SwerveControl:
    """
    What we want the swerve drive to do in terms of higher-level stuff rather
    than motor speeds and angles. 
    """
    fwd: float          # in range [-1, 1]
    strafe: float       # in range [-1, 1]
    rcw: float          # in range [-1, 1]
    
    def compute_states(self) -> PerModule[kinematics.SwerveModuleState]:
        (length, width) = c.DriveProperties.CHASSIS_DIMS
        dist = math.hypot(length, width)
        quadrants = {
            "F": self.strafe - (self.rcw * (length / dist)),
            "B": self.strafe + (self.rcw * (length / dist)),
            "L": self.fwd + (self.rcw * (width / dist)),
            "R": self.fwd - (self.rcw * (width / dist)),
        }
        return {
            key: self.compute_state(key, quadrants)
            for key in SWERVE_MODULE_TAGS
        }
    
    def compute_state(self, key, quadrants) -> kinematics.SwerveModuleState:
        [xCom, yCom] = [ quadrants[c] for c in key ]
        speed = math.hypot(xCom, yCom)
        angle = math.degrees(math.atan2(xCom, yCom))
        return kinematics.SwerveModuleState(speed, angle)

    @classmethod
    def default(cls):
        return cls(fwd = 0.0, strafe = 0.0, rcw = 0.0)

class SwerveDrive:

    # All of swerve modules (to be injected)
    swerveModuleFL: SwerveModule
    swerveModuleFR: SwerveModule
    swerveModuleBL: SwerveModule
    swerveModuleBR: SwerveModule

    # A list of refs to all the modules
    swerveModules: PerModule[SwerveModule] = None

    # The intended vectors for controlling the swerve modules
    _controlIntent: t.Union[SwerveControl, None] = None

    # A function to provide control intents, which can be overriden by _controlIntent
    # if it isn't null
    # If both are null, it will use SwerveControl.default()
    _controlFunction: t.Callable[[], t.Union[SwerveControl, None]] = lambda: None

    def setup(self):
        print("SwerveDrive setup")
        self.swerveModules = {
            tag: getattr(self, f"swerveModule{tag}")
            for tag in SWERVE_MODULE_TAGS
        }

    def execute(self):
        intent = self._controlIntent
        if intent == None:
            intent = self._controlFunction()
            if intent == None:
                intent = SwerveControl.default()
        print(f"actually running with intent {intent}")
        states = intent.compute_states()
        for key, module in self.swerveModules:
            module.setDesiredState(states[key])
        for _, module in self.swerveModules:
            module.execute()

    def set_intent(self, intent: t.Union[SwerveControl, None]):
        self._controlIntent = intent
    
    def set_intent_function(self, intent_function: t.Callable[[], t.Union[SwerveControl, None]]):
        self._controlFunction = intent_function
