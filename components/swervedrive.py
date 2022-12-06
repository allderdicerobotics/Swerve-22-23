import math
import typing as t

from magicbot import magiccomponent
from swervemodule import SwerveModule

import wpilib
import rev

import component_constants as c

class SwerveControlT(t.TypedDict):
    """
    A type representing a dictionary with the values that define what
    we want the swerve drive to do.
    """
    fwd: float          # [-1, 1]
    strafe: float
    rcw: float

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
    controlIntent: t.

    def setup(self):
        self.swerveModules = [
            self.swerveModuleFL,
            self.swerveModuleFR,
            self.swerveModuleBL,
            self.swerveModuleBR,
        ]


