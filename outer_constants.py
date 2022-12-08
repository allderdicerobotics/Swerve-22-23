# Constants for anything other than components

from wpilib import AnalogInput

# Hardware
class Hw:
    swerve_cfg = {
        "FL": {
            "driveMotor": (5,),
            "turningMotor": (6,),
            "turningEncoder": { "devInput": AnalogInput(0) },
        },
        "FR": {
            "driveMotor": (3,),
            "turningMotor": (4,),
            "turningEncoder": { "devInput": AnalogInput(2) },
        },
        "BL": {
            "driveMotor": (10,),
            "turningMotor": (9,),
            "turningEncoder": { "devInput": AnalogInput(1) },
        },
        "BR": {
            "driveMotor": (12,),
            "turningMotor": (11,),
            "turningEncoder": { "devInput": AnalogInput(3) },
        },
    }
