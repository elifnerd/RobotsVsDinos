class Dinosaur:
    
    def __init__(self, health):
        self.name = 'Boethiah the Becklespinax'
        self.health = health
        self.attack_power = 30

    def attack_robot(self, robot):
        robot -= self.attack_power