import math
import typing as t

from magicbot import magiccomponent
from swervemodule import SwerveModule

import wpilib
import rev

import component_constants as c

class SwerveDrive:

    # All of swerve modules
    swerveModuleFL: SwerveModule
    swerveModuleFR: SwerveModule
    swerveModuleBL: SwerveModule
    swerveModuleBR: SwerveModule

    # A list of refs to all the modules
    swerveModules: t.List[SwerveModule]

    # The dimensions of the chassis
    chassisDims: t.Tuple[float, float] = c.Swerve

    def setup(self):
        self.swerveModules = [
            self.swerveModuleFL,
            self.swerveModuleFR,
            self.swerveModuleBL,
            self.swerveModuleBR,
        ]

