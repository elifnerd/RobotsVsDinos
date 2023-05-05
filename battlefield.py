from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    
    def __init__(self):
        self.name = 'The Soul Cairn'
        self.dinosaur = Dinosaur(150)
        self.robot = Robot(300)
       
    def run_game(self):
        print("Initializing sequence...")

    def display_welcome(self):
        print(f'Hello to all monster enthusiasts and welcome to {self.name} ! For todays Monster Showdown, weve got a doozy of a show for you. A battle between naturemade and manmade monsters!')
        print(f'Up first we have our manmade monster, a lovely little dinosaur named {self.dinosaur.name}.')
        print(f'And her opponent! A robot that his loving fans refer to as {self.robot.name}!')
        print("Nature or mankind - who will win? Stay tuned to find out.")

    def battle_phase_one(self):
        self.robot.hp = self.dinosaur.attack_robot(self.robot.hp)
        self.dinosaur.health = self.robot.attack_dino(self.dinosaur.health)
        print(f'{self.dinosaur.name} attacks first with a whopping {self.dinosaur.attack_power} damage!')
        print(f'Ghorbash is now at {self.robot.hp} health points! He retaliates with {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power} damage.')

    def display_winner(self):
        pass
