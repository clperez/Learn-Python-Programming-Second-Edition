
# Creating my objects as dictionaries.
frodo = {
    'name' : 'Frodo Bolson',
    'race': 'hobbit',
    'skills': {
        'combat': 5,
        'misile': 10
    }
}

gandalf = {
    'name' : 'Gandalf',
    'race': 'Human',
    'skills': {
        'combat': 7,
        'misile': 7,
        'magic': 10
    }
}

print(frodo)
print(id(frodo))
print(type(frodo))

print(gandalf)
print(id(gandalf))
print(type(gandalf))

# Much better if i create a class

class Character:

    def __init__(self, name, race, **kvargs):
        self.name = name
        self.race = race
        self.skills = kvargs


frodo = Character('Frodo bolson', 'Hobbit',  'combat' = 5, 'misile'= 10 )
gandalf = Character('Gandalf', 'Human', { 'combat': 7, 'misile': 7, 'magic': 10 })


