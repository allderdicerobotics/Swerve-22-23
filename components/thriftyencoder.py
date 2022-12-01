import math

from wpimath import geometry
from wpilib import AnalogInput
import component_constants as c

class ThriftyEncoder:
    devInput : AnalogInput
    rotOffset : geometry.Rotation2d = geometry.Rotation2d()
    readVoltageMax : float = c.Encoders.STD_VOLTAGE_MAX

    def setup(self):
        self.standardReadVoltageMax = 4.8
    
    def getAngleRaw(self):
        voltage = self.devInput.getVoltage()
        normalized_reading = voltage / self.readVoltageMax
        angle_radians = normalized_reading * 2 * math.PI
        return geometry.Rotation2d(angle_radians) 

    def getAngle(self):
        return self.getAngleRaw() + self.rotOffset
        
