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
        print(f'Hello to all monster enthusiasts and welcome to {self.name} ! For todays Monster Mayhem, weve got a doozy of a show for you. A battle between naturemade and manmade monsters!')
        print(f'Up first we have our manmade monster, a lovely little dinosaur named {self.dinosaur.name}.')
        print(f'And her opponent! A robot that his loving fans refer to as {self.robot.name}!')
        print("Nature or mankind - who will win? Stay tuned to find out.")

    def battle_phase_one(self):
        self.dinosaur.health -= self.robot.active_weapon.attack_power
        self.robot.hp -= self.dinosaur.attack_power
        print(f'{self.dinosaur.name} attacks first with a whopping {self.dinosaur.attack_power} damage!')
        print(f'{self.robot.name} is now at {self.robot.hp} health points! He retaliates with {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power} damage.')
        print(f'{self.dinosaur.name} was hit! Her health points are down to {self.dinosaur.health}!')

    def battle_phase_two(self):
        self.dinosaur.health -= self.robot.active_weapon.attack_power
        self.robot.hp -= self.dinosaur.attack_power
        print(f'Damaging blows! {self.dinosaur.name} attacks again! {self.robot.name} now has {self.robot.hp} health points while {self.dinosaur.name} is slowing down with {self.dinosaur.health}.')

    def battle_phase_three(self):
        self.dinosaur.health -= self.robot.active_weapon.attack_power
        self.robot.hp -= self.dinosaur.attack_power
        print(f'Sadly, this is the end of the road for dear {self.dinosaur.name} who has {self.dinosaur.health} health points while her opponent still has {self.robot.hp} health points remaining! She fought bravely but was no match for the Iron Fist!')

    def display_winner(self):
        print(f'The winner of this round of Monster Mayhem is {self.robot.name}! Tune in on Monday to see who he will take on next!')
