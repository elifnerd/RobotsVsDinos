from weapon import Weapon

class Robot:
    
    def __init__(self, hp):
        self.name = 'Ghorbash the Iron Hand'
        self.hp = hp
        self.active_weapon = Weapon()
        
    def attack(self, dinosaur):
        self.attack_power = self.active_weapon.attack_power
        self.dinosaur = dinosaur