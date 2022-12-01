import math
import typing as t

from magicbot import magiccomponent
from swervemodule import SwerveModule

class SwerveDrive:

    # All of swerve modules
    swerveModuleFL: SwerveModule
    swerveModuleFR: SwerveModule
    swerveModuleBL: SwerveModule
    swerveModuleBR: SwerveModule

    # A list of refs to all the modules
    swerveModules: t.List[SwerveModule]

    # Desired module states
    

    def setup(self):
        self.swerveModules = [
            self.swerveModuleFL,
            self.swerveModuleFR,
            self.swerveModuleBL,
            self.swerveModuleBR,
        ]
