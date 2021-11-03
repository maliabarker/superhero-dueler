from os import name
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, Ability):
        pass

    def attack(self):
        pass

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        heros = [self.name, opponent.name]
        winner = random.choice(heros)
        if winner == heros[0]:
            return f'{winner} defeats {heros[1]}'
        elif winner == heros[1]:
            return f'{winner} defeats {heros[0]}'



if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  my_hero = Hero("Grace Hopper", 200)
  print(my_hero.name)
  print(my_hero.current_health)
  other_hero = Hero("Antman")
  print(my_hero.fight(other_hero))