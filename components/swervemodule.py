import wpilib
from wpimath import controller, kinematics, trajectory
import math
import rev
from thriftyencoder import ThriftyEncoder

class SwerveModule:
    driveMotor: rev.CANSparkMax
    turningMotor: rev.CANSparkMax

    driveEncoder: rev.RelativeEncoder
    turningEncoder : ThriftyEncoder

    drivePIDController: rev.SparkMaxPIDController
    turningPIDController: controller.ProfiledPIDController

    driveFeedForward: controller.SimpleMotorFeedforwardMeters
    turnFeedForward: controller.SimpleMotorFeedforwardMeters
    
    def setup(self):
        self.turningPIDController.enableContinuousInput(-math.pi, math.pi)
        self.driveEncoder = self.driveMotor.getEncoder()
        self.drivePIDController = self.driveMotor.getPIDController()
    def getState(self):
        return kinematics.SwerveModuleState(self.driveEncoder.getVelocity(),self.turningEncoder.getAngle())
    def setDesiredState(self,desiredState):
        self.state = kinematics.SwerveModuleState.optimize(desiredState,self.turningEncoder.getAngle())
        driveFeedforwardOut = self.driveFeedForward.calculate(self.state.speed_fps)
        turnOutput = self.turningPIDController.calculate(self.turningPIDController.getSetpoint().velocity)