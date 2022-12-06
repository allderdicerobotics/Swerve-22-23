import wpilib
from magicbot import MagicRobot
from robotcontainer import RobotContainer
from swervedrive import SwerveDrive
from swervemodule import SwerveModule

# Main robot class
class FRCRobot(MagicRobot):
    drivetrain: SwerveDrive

    drivetrain_swerveModuleFL: SwerveModule
    drivetrain_swerveModuleFR: SwerveModule
    drivetrain_swerveModuleBL: SwerveModule
    drivetrain_swerveModuleBR: SwerveModule

    def createObjects(self):
        self.drivetrain = SwerveDrive()
        self.drivetrain_swerveModuleFL = ...
        self.drivetrain_swerveModuleFR = ...
        self.drivetrain_swerveModuleBL = ...
        self.drivetrain_swerveModuleBR = ...
        

# Main section
if __name__ == "__main__":
    wpilib.run(FRCRobot)
