import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero_name):
        self.heroes.append(hero_name)

    def remove_hero(self, hero_name):
        foundHero = False

        for hero in self.heroes:
            if hero.name == hero_name:
                self.heroes.remove(hero)
                foundHero = True

        if not foundHero:
            return 0


    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        living_heros = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heros.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heros) > 0 and len(living_opponents) > 0:
            self_fighter = random.choice(self.heroes)
            other_fighter = random.choice(other_team.heroes)
            fight = self_fighter.fight(other_fighter)
            if fight == f'{self_fighter.name} defeated {other_fighter.name}!':
                living_opponents.remove(other_fighter)
            elif fight == f'{other_fighter.name} defeated {self_fighter.name}!':
                living_heros.remove(self_fighter)
            elif fight == f'{self_fighter.name} and {other_fighter.name} defeated eachother. Draw!':
                living_heros.remove(self_fighter)
                living_opponents.remove(other_fighter)

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            print(f'{hero.name} Kills/Deaths {hero.kills}:{hero.deaths}')
            # if hero.deaths == 0:
            #     print(f'{hero.name} Kills/Deaths:{hero.kills}:0')
            # else:
            #     kd = hero.kills / hero.deaths
            #     print(f'{hero.name} Kills/Deaths:{kd}')