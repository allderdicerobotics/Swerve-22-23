from wpilib import Joystick
from swervedrive import SwerveControl

class OI:
    driver: Joystick = Joystick(0)

    def get_swerve_intent(self):
        return SwerveControl(
            fwd = self.driver.getRawAxis(0),
            strafe = self.driver.getRawAxis(1),
            rcw = 0.0,
        )
