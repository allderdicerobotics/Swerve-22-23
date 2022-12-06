import math
import typing as t

from magicbot import magiccomponent
from swervemodule import SwerveModule

import wpilib
import rev
import attrs

import component_constants as c

@attrs.define
class SwerveControl:
    """
    What we want the swerve drive to do in terms of higher-level stuff rather
    than motor speeds and angles. 
    """
    fwd: float          # in range [-1, 1]
    strafe: float       # in range [-1, 1]
    rcw: float          # in range [-1, 1]

    def compute_speeds(self) -> t.List[float]: ...

    def compute_angles(self) -> t.List[float]: ...

class SwerveDrive:

    # All of swerve modules (to be injected)
    swerveModuleFL: SwerveModule
    swerveModuleFR: SwerveModule
    swerveModuleBL: SwerveModule
    swerveModuleBR: SwerveModule

    # A list of refs to all the modules
    swerveModules: t.List[SwerveModule]

    # The dimensions of the chassis
    chassisDims: t.Tuple[float, float] = c.DriveProperties.CHASSIS_DIMS

    # The intended vectors for controlling the swerve modules
    controlIntent: SwerveControlT

    def setup(self):
        self.swerveModules = [
            self.swerveModuleFL,
            self.swerveModuleFR,
            self.swerveModuleBL,
            self.swerveModuleBR,
        ]


