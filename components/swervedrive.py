import math
import typing as t

from magicbot import magiccomponent
from swervemodule import SwerveModule

from wpimath import kinematics

import wpilib
import rev
import attrs

import component_constants as c

T = t.TypeVar("T")
PerModule = t.Dict[t.Literal["FL", "FR", "BL", "BR"], T]

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
            for key in ("FL", "FR", "BL", "BR")
        }
    
    def compute_state(self, key, quadrants) -> kinematics.SwerveModuleState:
        [xCom, yCom] = [ quadrants[c] for c in key ]
        speed = math.hypot(xCom, yCom)
        angle = math.degrees(math.atan2(xCom, yCom))
        return kinematics.SwerveModuleState(speed, angle)

class SwerveDrive:

    # All of swerve modules (to be injected)
    swerveModuleFL: SwerveModule
    swerveModuleFR: SwerveModule
    swerveModuleBL: SwerveModule
    swerveModuleBR: SwerveModule

    # A list of refs to all the modules
    swerveModules: PerModule[SwerveModule]

    # The intended vectors for controlling the swerve modules
    controlIntent: SwerveControl

    def setup(self):
        self.swerveModules = {
            "FL": self.swerveModuleFL,
            "FR": self.swerveModuleFR,
            "BL": self.swerveModuleBL,
            "BR": self.swerveModuleBR,
        }

    def execute(self):
        states = self.controlIntent.compute_states()
        for key, module in self.swerveModules:
            module.setDesiredState(states[key])
        for _, module in self.swerveModules:
            module.execute()
