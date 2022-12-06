from components import swervedrive
import wpilib

class RobotContainer:
    def __init__(self) -> None:
        self.drive = swervedrive()
        self.controller = wpilib.Joystick(0)
