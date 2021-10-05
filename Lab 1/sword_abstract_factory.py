import time


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


class DemonLord:
    def __str__(self):
        return 'Return of the Demon Lord'

    def action(self):
        return '.... killed the Demon Lord'


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


class DragonKing:

    def __str__(self):
        return 'Return of the King of Dragons'

    def action(self):
        return ' killed the King of Dragons'


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

    def initiate_the_world(self):
        try:
            if self.character.profession == 'SwordsMan':
                generate_world = SwordsManWorld(self.character)
                time.sleep(2)
                self.hero = generate_world.make_character()
                time.sleep(2)
                self.enemy = generate_world.make_enemy()
            else:
                generate_world = MagicianWorld(self.character)
                self.hero = generate_world.make_character()
                self.enemy = generate_world.make_enemy()
        except:
            print('Invalid Speciality')

    def play(self):
        if self.character.profession == 'SwordsMan':
            time.sleep(2)
            self.hero.kill_demon_lord(self.enemy)
        else:
            time.sleep(2)
            self.hero.kill_king_dragons(self.enemy)


# def main():
#     player = Player()
#     player.create_character(profession='Swords man', special_attribute='fire',
#                             cultivation_path='Legendary swallow path')
#     character = player.character
#

# if __name__ == '__main__':
#     main()
