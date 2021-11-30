import time
from ..Lab2.adapter_method import MonsterSpawn
from ..Lab3.strategy_pattern import Strategy


# An improvised decorator
def decorator_action(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        return '.... killed the great evil!!'
    return inner


class DemonLord:

    def __str__(self):
        return 'The Demon Lord appeared...'

    @decorator_action
    def action(self):
        return self


class DragonKing:

    def __str__(self):
        return 'The King of Dragons appeared...'

    @decorator_action
    def action(self):
        return self


class SwordsMan:
    def __init__(self, character):
        self.character = character

    def __str__(self):
        return 'The character began his path in the sword world.'

    def kill_demon_lord(self, demon_lord):
        print(f'{self.character.name}' + ' after a big battle...')
        time.sleep(2)
        print(demon_lord.action())
        return demon_lord.action()


class Magician:
    def __init__(self, character):
        self.character = character

    def __str__(self):
        return 'The character began his path in the world of magic.'

    def kill_king_dragons(self, king_dragons):
        print(f'{self.character.name}' + ' after a big battle...')
        time.sleep(2)
        print(king_dragons.action())
        return king_dragons.action()


class SwordsManWorld:
    def __init__(self, character):
        self.character = character

    def __str__(self):
        return 'Swords Man World'

    def make_character(self):
        swordman = SwordsMan(self.character)
        print(swordman)
        return swordman

    def make_enemy(self):
        enemy = DemonLord()
        print(enemy)
        return enemy


class MagicianWorld:
    def __init__(self, character):
        self.character = character

    def __str__(self):
        return 'Magic World'

    def make_character(self):
        magician = Magician(self.character)
        print(magician)
        return magician

    def make_enemy(self):
        return DragonKing()


class PathDecision:

    def __init__(self, character):
        self.character = character
        self.hero = None
        self.enemy = None

    def monster_spawn_black_forest(self):

        ''' Adapter method '''

        print('Entering the dark forest...')
        time.sleep(1)
        monster_spawn = MonsterSpawn()
        print(monster_spawn.spawn_process())
        time.sleep(1)
        print('Climbing the black mountain...')

    def initiate_the_world(self):
        try:
            if self.character.profession == 'SwordsMan':
                generate_world = SwordsManWorld(self.character)
                time.sleep(2)
                self.hero = generate_world.make_character()
                time.sleep(2)
                self.monster_spawn_black_forest()
                time.sleep(2)
                print('You entered the misty mountains and were cursed....')
                time.sleep(2)
                strategy = Strategy('SwordsMan')
                strategy.strategy_chooser()
                time.sleep(2)
                print('Traveling to your final destination...')
                time.sleep(2)
                self.enemy = generate_world.make_enemy()
            else:
                generate_world = MagicianWorld(self.character)
                time.sleep(2)
                self.hero = generate_world.make_character()
                time.sleep(2)
                self.monster_spawn_black_forest()
                time.sleep(2)
                print('You entered the misty mountains and were cursed....')
                time.sleep(2)
                strategy = Strategy('Magician')
                strategy.strategy_chooser()
                time.sleep(2)
                print('Traveling to your final destination...')
                time.sleep(2)
                self.enemy = generate_world.make_enemy()
        except:
            print('Invalid Speciality')

    def play(self):
        if self.character.profession == 'SwordsMan':
            time.sleep(2)
            self.hero.kill_demon_lord(self.enemy)
            print('Mission complete!!!')
        else:
            time.sleep(2)
            self.hero.kill_king_dragons(self.enemy)
            print('Mission complete!!!')

