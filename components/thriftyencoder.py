import math
from wpimath import geometry
from wpilib import AnalogInput
import components.component_constants as c
import attrs

@attrs.define
class ThriftyEncoder:
    devInput : AnalogInput = None
    rotOffset : geometry.Rotation2d = geometry.Rotation2d()
    readVoltageMax : float = c.Encoders.STD_VOLTAGE_MAX
    
    def getAngleRaw(self):
        voltage = self.devInput.getVoltage()
        normalized_reading = voltage / self.readVoltageMax
        angle_radians = normalized_reading * 2 * math.pi
        return geometry.Rotation2d(angle_radians) 

    def getAngle(self):
        return self.getAngleRaw() + self.rotOffset

    def resetPosition(self):
        self.rotOffset = self.getAngleRaw()
