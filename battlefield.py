from robot import Robot

from weapon import Weapon

from dinosaur import Dinosaur

class Battlefield:
    
    def __init__(self):
        self.name = 'The Soul Cairn'
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        print("Initializing sequence...")     

    def display_welcome(self):
        print("Hello and welcome to ! For today's Monster Showdown, we've got a doozy of a show for you. A battle between nature-made and man-made monsters! Who will win? Stay tuned to find out.")

    def battle_phase_one(self):
        print(f'Boethiah attacks first. Its a hit! Ghorbash is down to {self.dinosaur.attack_robot}')

    def display_winner(self):
        pass
