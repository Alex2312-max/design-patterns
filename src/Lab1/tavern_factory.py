import time


class Tavern:

    class Party:

        def __init__(self):
            self.drink = 'Drink Wine'
            self.dance = 'Dance all night...'
            self.break_furniture = 'Break the table, chair, nose....'

        def __str__(self):
            print('Let the party begin:\n')
            time.sleep(1)
            print(self.drink)
            time.sleep(1)
            print(self.dance)
            time.sleep(1)
            print(self.break_furniture)
            time.sleep(1)
            return 'You drank too much and now you are fall to sleep....'

    def create_party(self, decision):
        if decision == '1':
            print(self.Party())
            # return self.Party
        else:
            return 'Returning to saving the world'


