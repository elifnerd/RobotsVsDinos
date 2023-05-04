class Weapon:
    
    def __init__(self):
        self.name = 'Lightsaber'
        self.attack_power = 50

    def swing(self, Dinosaur):
        Dinosaur.health -= self.attack_power

