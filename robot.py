from weapon import Weapon


class Robot:
    
    def __init__(self, hp):
        self.name = 'Ghorbash the Iron Hand'
        self.hp = hp
        self.active_weapon = Weapon()
        
    def attack_dino(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power