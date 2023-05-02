from robot import Robot

from dinosaur import Dinosaur

class Battlefield:
    
    def __init__(self):
        self.name = 'the Soul Cairn'
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def run_game(self):
        print("Initializing sequence...")     

    def display_welcome(self):
        print("Hello and welcome to all Monster enthusiasts! For today's Monster Showdown, we've got a doozy of a show for you. A battle between nature-made and man-made monsters! Who will win? Stay tuned to find out.")

    def battle_phase(self):
        self.robot.attack_dino
        self.dinosaur.attack_robot
        print(f'Ghorbash has attacked Boethiah! Our favorite dinos health is now at {Robot.attack_dino}!')
        print(f'Boethiah has retaliated! Ghorbash the Iron Hand is down to {Dinosaur.attack_robot}!')

    def display_winner(self):
        pass
