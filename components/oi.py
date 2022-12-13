from wpilib import Joystick
from components.swervedrive import SwerveControl

class OI:
    driver: Joystick

    def get_swerve_intent(self):
        control = SwerveControl(
            fwd = self.driver.getRawAxis(0),
            strafe = self.driver.getRawAxis(1),
            rcw = 0.0,
        )
        print(f"intent: {control}")
        return control
    
    def execute(self):
        pass
