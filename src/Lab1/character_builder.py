class Character:
    def __init__(self, name):
        self.name = name
        self.profession = None
        self.special_attribute = None
        self.cultivation_path = None

    def __str__(self):
        info = (f'Name: {self.name}',
                f'Profession: {self.profession}',
                f'Special Attribute: {self.special_attribute}',
                f'Cultivation Path: {self.cultivation_path}')
        return '\n'.join(info)


class CharacterBuilder:
    def __init__(self, name):
        self.character = Character(name)

    def select_profession(self, profession):
        self.character.profession = profession

    def select_special_attribute(self, special_attribute):
        self.character.special_attribute = special_attribute

    def select_cultivation_path(self, cultivation_path):
        self.character.cultivation_path = cultivation_path


class Player:
    def __init__(self):
        self.builder = None

    def create_character(self, profession, special_attribute, cultivation_path, name):
        self.builder = CharacterBuilder(name)
        self.builder.select_profession(profession)
        self.builder.select_special_attribute(special_attribute)
        self.builder.select_cultivation_path(cultivation_path)

    @property
    def character(self):
        return self.builder.character


# def main():
#
#     player = Player()
#     player.create_character(profession='Swords man', special_attribute='fire', cultivation_path='Legendary swallow path')
#     character = player.character
#     print(character)
#
#
# if __name__ == '__main__':
#     main()
