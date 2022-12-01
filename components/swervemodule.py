import wpilib
from wpimath import controller, kinematics, trajectory
import math
import rev

class SwerveModule:
    driveMotor: rev.CANSparkMax
    turningMotor: rev.CANSparkMax

    relativeEncoder: rev.RelativeEncoder
    # thriftyEncoder : 

    drivePIDController: rev.SparkMaxPIDController
    turningPIDController: controller.ProfiledPIDController

    driveFeedForward: controller.SimpleMotorFeedforwardMeters
    turnFeedForward: controller.SimpleMotorFeedforwardMeters
    
    def setup(self):
        self.turningEncoder 
        self.turningPIDController.enableContinuousInput(-math.pi, math.pi)
        self.driveEncoder = self.driveMotor.getEncoder()
        self.drivePIDController = self.driveMotor.getPIDController()
    def getState(self):
        return kinematics.SwerveModuleState(self.driveEncoder.getVelocity(),self)