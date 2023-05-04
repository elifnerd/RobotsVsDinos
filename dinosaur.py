from robot import Robot

class Dinosaur:
    
    def __init__(self):
        self.name = 'Boethiah the Becklespinax'
        self.health = 150
        self.attack_power = 30
        self.attack_robot = Robot()

    def attack_robot(self, robot, hp):
        robot.hp -= Dinosaur.attack_power
        print(robot.hp)
        

    