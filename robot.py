import typing as t

import outer_constants as oc

import wpilib
from magicbot import MagicRobot
from components import swervedrive
from components.swervemodule import SwerveModule
from components.oi import OI
from arguments import Arguments
from components.thriftyencoder import ThriftyEncoder
import rev

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

    drivetrain_swerveModuleFL_driveMotor: rev.CANSparkMax
    drivetrain_swerveModuleFL_turningMotor: rev.CANSparkMax
    drivetrain_swerveModuleFL_turningEncoder: ThriftyEncoder

    drivetrain_swerveModuleFR_driveMotor: rev.CANSparkMax
    drivetrain_swerveModuleFR_turningMotor: rev.CANSparkMax
    drivetrain_swerveModuleFR_turningEncoder: ThriftyEncoder

    drivetrain_swerveModuleBL_driveMotor: rev.CANSparkMax
    drivetrain_swerveModuleBL_turningMotor: rev.CANSparkMax
    drivetrain_swerveModuleBL_turningEncoder: ThriftyEncoder

    drivetrain_swerveModuleBR_driveMotor: rev.CANSparkMax
    drivetrain_swerveModuleBR_turningMotor: rev.CANSparkMax
    drivetrain_swerveModuleBR_turningEncoder: ThriftyEncoder

    oi_driver: wpilib.Joystick

    def createObjects(self):
        self.setupOI()
        self.setupSwerve()
    
    def setup(self):
        self.setupSwerveControl()

    def setupSwerve(self):
        self.drivetrain = SwerveDrive()
        self.setupSwerveModules()
        #| Cannot do this until OI object is set up |# self.setupSwerveControl()
    
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
                elif isinstance(cfg, (...).__class__):
                    raise Exception(
                        f"You need to specify the swerve configuration for {tag}/{subprop}. "
                    )
                else:
                    value = item_class(*cfg)
                setattr(self, f"{module_prop}_{subprop}", value)

    def setupSwerveControl(self):
        self.drivetrain.set_intent_function(lambda: self.oi.get_swerve_intent())
    
    def setupOI(self):
        self.oi_driver = wpilib.Joystick(oc.OI.driver_port)

# Main section
if __name__ == "__main__":
    wpilib.run(FRCRobot)
