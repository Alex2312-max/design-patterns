import time

WARNING = 'You picked an inappropriate way to handle the curse according to your powers.'


class Strategy:
    def __init__(self, class_hero):
        self.class_type = class_hero

    def swordman_curse(self):
        if self.class_type == 'Magician':
            print('.....')
            time.sleep(10)
            print(WARNING)
            return 'You escaped the curse with a lot of struggle and were stunned for 10 seconds.'

        return 'You escaped the curse easily by drinking the potion.'

    def magician_curse(self):
        if self.class_type == 'SwordsMan':
            print('.....')
            time.sleep(10)
            print(WARNING)
            time.sleep(2)
            return 'You escaped the curse with a lot of struggle by casting the spell and were stunned for 10 seconds.'

        return 'You escaped the curse easily by casting a healing spell.'

    def method_wrapper(self, strategy):
        return strategy()

    def strategy_chooser(self):
        while True:
            word = None
            while not word:
                word = input('Do you want to away from curse?')
                if word == 'Quit!':
                    print('You died.')
                    return False
                strategy_picked = None
                strategies = {
                    '1': self.swordman_curse,
                    '2': self.magician_curse
                    }
                while strategy_picked not in strategies.keys():
                    strategy_picked = input('Choose strategy: \n' +
                                            '1. Drink a potion\n' +
                                            '2. Cast a spell\n')
                try:
                    strategy = strategies[strategy_picked]
                    print(self.method_wrapper(strategy))
                    return True
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))

