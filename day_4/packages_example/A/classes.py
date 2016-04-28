
class Animal(object):
    pass
    

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return "I'm Walking"

class Poacher(Person):
    
    def __init__(self, name, age, **kwargs):
        Person.__init__(self, name, age)
        self.gun = kwargs.get('gun', 'AK-47')
        self.loc = kwargs.get('loc', 'Nairobi')
        self.game_park = kwargs.get('game_park', 'Tsavo')
        self.fav = kwargs.get('fav', 'Elephant')

        # print "Args", args
        # # for args
        # if args[0]:
        #     self.loc = args[0]
        # if args[1]:
        #     self.gun = args[1]

class Tourist(object):
    pass

p = Person('Jane', 23)
pc = Poacher('Joe', 45, gun='Rifle', game_park='NNP', loc='Mombasa')
# pc2 = Poacher('Joe', 45, 'Nairobi', 'AK-47', gun='Bonoko')

# print pc.name, pc.age, pc.gun, pc.fav

# print pc2.gun














