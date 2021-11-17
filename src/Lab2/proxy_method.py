class Bag:
    def __init__(self):
        self.materials = ['bread', 'water', 'potions', 'hat']

    def read(self):
        print('There are {} elements in your bag: {}'.format(len(self.materials), ' '.join(self.materials)))

    def add(self, material):
        self.materials.append(material)
        print('Added material {}'.format(material))


class InfoBag:

    def __init__(self):
        self.protected = Bag()
        self.secret = 'bunny'

    def read(self):
        self.protected.read()

    def add(self, material):
        sec = input('what is the secret? ')
        self.protected.add(material) if sec == self.secret else print("That's wrong!")