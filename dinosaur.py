from robot import Robot

class Dinosaur:
    
    def __init__(self) -> None:
        self.name = 'Boethiah the Becklespinax'
        self.health = 120
        self.attack_power = 30
        self.attack_robot = Robot()

    def attack_robot(self, robot):
        robot.health -= self.attack_power
        print(f'Ghorbash has attacked Boethiah! Our favorite dinos health is now at {Robot.attack_dino}!')
    

