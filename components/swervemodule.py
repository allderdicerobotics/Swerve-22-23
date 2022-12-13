import wpilib
from wpimath import controller, kinematics, trajectory
import math
import rev
from components.thriftyencoder import ThriftyEncoder
from components.component_constants import DriveProperties


class SwerveModule:
    driveMotor: rev.CANSparkMax
    turningMotor: rev.CANSparkMax

    driveEncoder: rev.RelativeEncoder
    turningEncoder: ThriftyEncoder

    drivePIDController: rev.SparkMaxPIDController
    turningPIDController: controller.ProfiledPIDController = controller.ProfiledPIDController(1.1, 0, 0,
                                                                                              trajectory.TrapezoidProfile.Constraints(DriveProperties.MODULE_MAX_ANGULAR_VELOCITY,
                                                                                                                                      DriveProperties.MODULE_MAX_ANGULAR_ACCELERATION))


    driveFeedForward: controller.SimpleMotorFeedforwardMeters = controller.SimpleMotorFeedforwardMeters(0.33217,2.5407,0.52052)
    turnFeedForward: controller.SimpleMotorFeedforwardMeters = controller.SimpleMotorFeedforwardMeters(0.25,0.4)

    def setup(self):
        self.turningPIDController.enableContinuousInput(-math.pi, math.pi)
        self.driveEncoder = self.driveMotor.getEncoder()
        self.drivePIDController = self.driveMotor.getPIDController()

    def getState(self):
        return kinematics.SwerveModuleState(self.driveEncoder.getVelocity(), self.turningEncoder.getAngle())

    def setDesiredState(self, desiredState):
        self.state = kinematics.SwerveModuleState.optimize(
            desiredState, self.turningEncoder.getAngle())
        driveFeedforwardOut = self.driveFeedForward.calculate(
            self.state.speed_fps)

        turnOutput = self.turningPIDController.calculate(
            self.turningEncoder.getAngle().radians(), self.state.angle.radians())
        turnFeedforwardOut = self.turnFeedForward.calculate(
            self.turningPIDController.getSetpoint().velocity)
        driveMotorRPM = self.state.speed * 60 / math.pi / \
            DriveProperties.WHEEL_RADIUS / 2 * DriveProperties.DRIVE_WHEEL_GEAR_RATIO
        self.drivePIDController.setReference(driveMotorRPM, rev.CANSparkMax.ControlType.kVelocity,
                                             2, driveFeedforwardOut, rev.SparkMaxPIDController.ArbFFUnits.kVoltage)
        self.turningMotor.setVoltage(turnOutput+turnFeedforwardOut)

    def resetEncoders(self):
        self.driveEncoder.setPosition(0)
        self.turningEncoder.resetPosition()
