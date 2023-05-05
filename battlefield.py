from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon


class Battlefield:
    
    def __init__(self):
        self.name = 'The Soul Cairn'
        self.robot = Robot(300)
        self.dinosaur = Dinosaur(150)

        
    def run_game(self):
        print("Initializing sequence...")
        robot_new_health = self.robot.attack_dino(150)
        dino_new_health = self.dinosaur.attack_robot(300)

    def display_welcome(self):
        print(f'Hello to all monster enthusiasts and welcome to {self.name} ! For todays Monster Showdown, weve got a doozy of a show for you. A battle between naturemade and manmade monsters!')
        print(f'Up first we have our manmade monster, a lovely little dinosaur named {self.dinosaur.name}.')
        print(f'And her opponent! A robot that his loving fans refer to as {self.robot.name}!')
        print("Nature or mankind - who will win? Stay tuned to find out.")

    def battle_phase_one(self):
        print(f'{self.dinosaur.name} attacks first with a whopping {self.dinosaur.attack_power} damage!')
        print(f'Ghorbash is now at {self.robot_new_health}! He retaliates with {self.weapon.name} for {self.weapon.attack_power} damage.')

    def display_winner(self):
        pass
