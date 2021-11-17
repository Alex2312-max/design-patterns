import time


class MonsterSpawn:

    class Goblin:
        def __str__(self):
            return 'Goblin spawned.'

        def action_sword(self):
            return 'Goblin defeated, tooth of goblin obtained.'

    class GoblinMagician:
        def __str__(self):
            return 'Goblin magician appeared from portal.'

        def action_magic(self):
            return 'Goblin defeated, magic crystal obtained.'

    class Adapter:

        def __init__(self, obj, adapted_methods):
            self.obj = obj
            self.__dict__.update(adapted_methods)

        def __str__(self):
            return str(self.obj)

    def spawn_process(self):
        objects = []
        goblin = self.Goblin()
        goblin_magician = self.GoblinMagician()
        objects.append(self.Adapter(goblin, dict(execute=goblin.action_sword)))
        objects.append(self.Adapter(goblin_magician, dict(execute=goblin_magician.action_magic)))

        for i in objects:
            time.sleep(1)
            print('{} {}'.format(str(i), i.execute()))
