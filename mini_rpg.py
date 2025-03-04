import config

class Dungeon:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

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
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def damage_target(self, target):
        self.target = target
        target.health -= self.attack
        return target.health

class Monster(Creature):
    pass

class Character(Creature):
    pass

class Sorcerer(Creature):
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

# Dungeon unit tests
# dungeon: Dungeon = Dungeon("Tomb of Minor Inconvenience", config.dungeon_rooms)
# print(f"WELCOME to the {dungeon.name}!")
# print(f"You enter the {dungeon.rooms["room_6"]["name"]}.")
# print(dungeon.rooms["room_6"]["description"])

# Creature unit tests
enemy: Monster = Monster("Goblin 1", 50, 5)
print(f"{enemy.name} - Health: {enemy.health} - Attack: {enemy.attack}")
character: Character = Character("Beastman", 100, 10)
print(f"{character.name} - Health: {character.health} - Attack: {character.attack}")

# Attack unit tests
character.damage_target(enemy)
print(f"{character.name} attacks {enemy.name} for {character.attack}.")
print(f"{enemy.name}'s health is now {enemy.health}.")