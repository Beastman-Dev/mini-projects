class Dungeon:
    def __init__(self, name):
        self.name = name
        self.rooms = {}

class Room:
    def __init__(self, name, length, width, description, exits, contents):
        self.name = name
        self.length = length
        self.width = width
        self.description = description
        self.exits = exits
        self.contents = contents

class Creature:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Monster(Creature):
    pass

class Character(Creature):
    pass

class Treasure:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Weapon(Treasure):
    pass

class Armor(Treasure):
    pass

dungeon: Dungeon = Dungeon("Tomb of Minor Inconvenience")
print(dungeon.name)

room_one: Room = Room("Main Entrance", 30, 20, "description", 3, "contents")
print(room_one.description)