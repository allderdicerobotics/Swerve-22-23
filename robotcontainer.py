from components import swervedrive
import wpilib

class RobotContainer:
    def __init__(self) -> None:
        self.drive = swervedrive()
        self.controller = wpilib.Joystick(0)
    def getDriveCommand(self) -> swervedrive:
        return swervedrive(
            self.drive,
            lambda: self.controller.getRawAxis(0),
            lambda: self.controller.getRawAxis(1),
        )