import wpilib
from wpimath import controller, kinematics, trajectory
import rev

class SwerveModule:
    driveMotor : rev.CANSparkMax
    turningMotor : rev.CANSparkMax

    relativeEncoder : rev.RelativeEncoder
    # thriftyEncoder : 

    drivePIDController : rev.SparkMaxPIDController
    turningPIDController : controller.ProfiledPIDController

    driveFeedForward : controller.SimpleMotorFeedforwardMeters
    turnFeedForward : controller.SimpleMotorFeedforwardMeters
    