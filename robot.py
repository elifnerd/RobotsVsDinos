from weapon import Weapon


class Robot:
    
    def __init__(self):
        self.name = 'Ghorbash the Iron Hand'
        self.health = 300
        self.weapon = Weapon()
        
    def attack_dino(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power