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

    def damage_target(self, target, attack_power):
        self.target = target
        target.health -= attack_power
        return target.health

class Monster(Creature):
    pass

class Character(Creature):
    pass

class Sorcerer(Creature):
    def __init__(self, name, health, attack, mana):
        super().__init__(name, health, attack)
        self.mana = mana

    def cast_spell(self, target):
        self.target = target
        spell_power = int(input("How much mana would you like to spend? "))
        if spell_power > self.mana:
            print("You don't have enough mana!")
            return
        self.mana -= spell_power
        self.damage_target(target, spell_power)
        return spell_power
        # target.health -= self.attack
        # self.mana -= 10
        # return target.health

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
sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
print(f"{sorcerer.name} - Health: {sorcerer.health} - Attack: {sorcerer.attack} - Mana: {sorcerer.mana}")

# Attack unit tests
# character.damage_target(enemy, character.attack)
# print(f"{character.name} attacks {enemy.name} for {character.attack}.")
# print(f"{enemy.name}'s health is now {enemy.health}.")

# Cast spell unit tests
spell_power = sorcerer.cast_spell(enemy)
print(f"{sorcerer.name} casts a spell on {enemy.name} for {spell_power}.")
print(f"{enemy.name}'s health is now {enemy.health}.")
print(f"{sorcerer.name}'s mana is now {sorcerer.mana}.")