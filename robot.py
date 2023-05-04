from weapon import Weapon


class Robot:
    
    def __init__(self):
        self.name = 'Ghorbash the Iron Hand'
        self.hp = 300
        self.active_weapon = Weapon()
        
    def attack_dino(self, dinosaur, weapon):
        dinosaur.health -= self.active_weapon.attack_power
