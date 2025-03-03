class Dungeon:
    def __init__(self, name):
        self.name = name
        self.rooms = {}

# Room properties = name, description, search_results, exits, enemies, treasure
class Room:
    def __init__(self, name, description, search_results, exits, enemies, treasure):
        self.name = name
        self.description = description
        self.search_results = search_results
        self.exits = exits
        self.enemies = enemies
        self.treasure = treasure

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