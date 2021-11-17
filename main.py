import os

from src.Lab1.character_builder import Player
from src.Lab1.sword_abstract_factory import PathDecision
from src.Lab1.tavern_factory import Tavern

from src.Lab2.proxy_method import InfoBag

import time


def main():
    mapper = {
        '1': 'SwordsMan',
        '2': 'Magician'
    }

    print('Welcome to the Fantasy World!!!!')
    time.sleep(2)
    name = input('Enter a name for the character:\n')
    profession = input('Choose your profession:\n'
                       + '1. Sword Man\n'
                       + '2. Magician\n')
    special_attribute = input('Write an attribute:\n')
    cultivation_path = input('Choose a cultivation path: \n')
    player = Player()
    player.create_character(profession=mapper[profession], special_attribute=special_attribute,
                            cultivation_path=cultivation_path, name=name)

    while True:
        what_to_do = input('What do you want to do?\n'
                           + '1. Save the world\n'
                           + '2. Look in your bag\n'
                           + '3. Party all the night\n')

        if int(what_to_do) == 1:

            character = player.character
            path_decision = PathDecision(character)
            path_decision.initiate_the_world()
            time.sleep(1)
            path_decision.play()
            break

        if int(what_to_do) == 2:
            info = InfoBag()
            while True:
                print('1. Read list of element from your bag\n'
                      + ' 2. Add material\n'
                      + ' 3. quit')
                key = input('Choose option: ')
                if key == '1':
                    info.read()

                elif key == '2':
                    name = input('Choose material to add: ')
                    info.add(name)
                elif key == '3':
                    break
                else:
                    print('Unknown option: {}'.format(key))
        else:
            question = input('Do you really want to party?\n'
                             + '1. Yes\n'
                             + '2. No\n')
            tavern = Tavern()
            tavern.create_party(question)
            break


if __name__ == '__main__':
    main()
