import os
from character_builder import Player
from sword_abstract_factory import PathDecision
from tavern_factory import Tavern
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

    what_to_do = input('What do you want to do?\n'
                       + '1. Save the world\n'
                       + '2. Party all the night\n')

    if int(what_to_do) == 1:

        character = player.character
        path_decision = PathDecision(character)
        path_decision.initiate_the_world()
        path_decision.play()

    else:
        question = input('Do you really want to party?\n'
                         + '1. Yes\n'
                         + '2. No\n')
        tavern = Tavern()
        tavern.create_party(question)


if __name__ == '__main__':
    main()
