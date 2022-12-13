import typing as t

import outer_constants as oc

import wpilib
from magicbot import MagicRobot
import swervedrive
from swervemodule import SwerveModule
from oi import OI
from arguments import Arguments

# Just an alias because we need to import the whole module
SwerveDrive = swervedrive.SwerveDrive

# Main robot class
class FRCRobot(MagicRobot):
    drivetrain: SwerveDrive

    oi: OI

    drivetrain_swerveModuleFL: SwerveModule
    drivetrain_swerveModuleFR: SwerveModule
    drivetrain_swerveModuleBL: SwerveModule
    drivetrain_swerveModuleBR: SwerveModule

    def createObjects(self):
        self.setupSwerve()

    def setupSwerve(self):
        self.drivetrain = SwerveDrive()
        self.setupSwerveModules()
        self.setupSwerveControl()
    
    def setupSwerveModules(self):
        for tag in swervedrive.SWERVE_MODULE_TAGS:
            module_prop = f"drivetrain_swerveModule{tag}"
            for subprop in ("driveMotor", "turningMotor", "turningEncoder"):
                cfg = oc.Hw.swerve_cfg[tag][subprop]
                item_class = SwerveModule.__annotations__[subprop]
                if isinstance(cfg, dict):
                    value = item_class(**cfg)
                elif isinstance(cfg, Arguments):
                    value = item_class(*cfg.positional, **cfg.keyword)
                elif isinstance(cfg, Ellipsis):
                    raise Exception(
                        f"You need to specify the swerve configuration for {tag}/{subprop}. "
                    )
                else:
                    value = item_class(*cfg)
                setattr(self, f"{module_prop}_{subprop}", value)

    def setupSwerveControl(self):
        self.drivetrain.set_intent_function(self.oi.get_swerve_intent)

# Main section
if __name__ == "__main__":
    wpilib.run(FRCRobot)
