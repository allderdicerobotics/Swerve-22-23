import wpilib
from magicbot import MagicRobot
from robotcontainer import RobotContainer
# Main robot class
class FRCRobot(MagicRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()
    
    def createObjects(self):
        pass

# Main section
if __name__ == "__main__":
    wpilib.run(FRCRobot)
