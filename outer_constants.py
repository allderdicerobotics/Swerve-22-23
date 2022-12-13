# Constants for anything other than components

from wpilib import AnalogInput
import rev

kBrushless = rev._rev.CANSparkMaxLowLevel.MotorType.kBrushless

# Hardware
class Hw:
    swerve_cfg = {
        "FL": {
            "driveMotor": (5, kBrushless),
            "turningMotor": (6, kBrushless),
            "turningEncoder": { "devInput": AnalogInput(0) },
        },
        "FR": {
            "driveMotor": (3, kBrushless),
            "turningMotor": (4, kBrushless),
            "turningEncoder": { "devInput": AnalogInput(2) },
        },
        "BL": {
            "driveMotor": (10, kBrushless),
            "turningMotor": (9, kBrushless),
            "turningEncoder": { "devInput": AnalogInput(1) },
        },
        "BR": {
            "driveMotor": (12, kBrushless),
            "turningMotor": (11, kBrushless),
            "turningEncoder": { "devInput": AnalogInput(3) },
        },
    }

# Operator Interface *CONFIGURATION*
class OI:
    driver_port = 0
