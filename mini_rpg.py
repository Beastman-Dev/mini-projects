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
        self.current_health = health
        self.attack = attack

    def damage_target(self, target, attack_power):
        self.target = target
        target.current_health -= attack_power
        return target.current_health

class Monster(Creature):
    pass

class Character(Creature):
    pass

class Sorcerer(Creature):
    def __init__(self, name, health, attack, mana):
        super().__init__(name, health, attack)
        self.mana = mana
        self.current_mana = mana

    def cast_spell(self, target):
        self.target = target
        spell_power = int(input("How much mana would you like to spend? "))
        if spell_power > self.current_mana:
            print("You don't have enough mana!")
            return
        self.current_mana -= spell_power
        self.damage_target(target, spell_power)
        return spell_power

class Treasure:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Weapon(Treasure):
    pass

class Armor(Treasure):
    pass

class Potion(Treasure):
    def __init__(self, type, value, potency):
        self.type = type
        self.value = value
        self.potency = potency

    def add_to_inventory(self):
        pass

    def use_potion(self, imbiber):
        self.imbiber = imbiber
        if self.type == "health":
            if imbiber.current_health == imbiber.health:
                print(f"{imbiber.name} is already at full health!")
                return
            print(f"{imbiber.name} drinks a health potion and restores {self.potency} health.")
            imbiber.current_health += self.potency
            if imbiber.current_health > imbiber.health:
                imbiber.current_health = imbiber.health
        elif self.type == "mana":
            if not isinstance(imbiber, Sorcerer):
                print("Only sorcerers can use mana potions!")
                return
            if imbiber.current_mana == imbiber.mana:
                print(f"{imbiber.name} is already at full mana!")
                return
            print(f"{imbiber.name} drinks a mana potion and restore {self.potency} mana.")
            imbiber.current_mana += self.potency
            if imbiber.current_mana > imbiber.mana:
                imbiber.current_mana = imbiber.mana
        else:
            print("Invalid potion type!")



## Unit Tests

def create_dungeon_unit_tests():
    try:
        dungeon: Dungeon = Dungeon("Tomb of Minor Inconvenience", config.dungeon_rooms)
        if dungeon.name == "Tomb of Minor Inconvenience":
            return True
    except Exception as e:
        return e

def create_room_unit_tests():
    try:
        room: Room = Room("test_room", "A small room with a single door.", "You find a health potion!", ["north"], ["Goblin 1"], ["health potion"])
        if room.name == "test_room":
            return True
    except Exception as e:
        return e

def create_creature_unit_tests():
    try:
        enemy: Monster = Monster("Goblin 1", 50, 5)
        character: Character = Character("Beastman", 100, 10)
        sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
        if enemy.name == "Goblin 1" and character.name == "Beastman" and sorcerer.name == "Gandalf":
            return True
    except Exception as e:
        return e

def create_potion_unit_tests():
    try:
        health_potion: Potion = Potion("health", 10, 10)
        mana_potion: Potion = Potion("mana", 10, 10)
        if health_potion.type == "health" and mana_potion.type == "mana":
            return True
    except Exception as e:
        return e

def use_potion_unit_tests():
    try:
        fighter: Character = Character("Beastman", 100, 10)
        sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
        health_potion: Potion = Potion("health", 10, 10)
        mana_potion: Potion = Potion("mana", 10, 10)
        health_potion.use_potion(fighter)
        if fighter.current_health == 100:
            test_1 = True
        else:
            test_1 = False
        mana_potion.use_potion(sorcerer)
        if sorcerer.current_mana == 100:
            test_2 = True
        else:
            test_2 = False
        fighter.current_health = 80
        sorcerer.current_mana = 80
        health_potion.use_potion(fighter)
        if fighter.current_health == 90:
            test_3 = True
        else:
            test_3 = False
        mana_potion.use_potion(sorcerer)
        if sorcerer.current_mana == 90:
            test_4 = True
        else:
            test_4 = False
        if test_1 == True and test_2 == True and test_3 == True and test_4 == True:
            return True
    except Exception as e:
        return e

def attack_unit_tests():
    try:
        character: Character = Character("Beastman", 100, 10)
        enemy: Monster = Monster("Goblin 1", 50, 5)
        character.damage_target(enemy, character.attack)
        if enemy.current_health == 40:
            return True
    except Exception as e:
        return e

def cast_spell_unit_tests():
    try:
        enemy: Monster = Monster("Goblin 1", 50, 5)
        sorcerer: Sorcerer = Sorcerer("Gandalf", 100, 10, 100)
        spell_power = sorcerer.cast_spell(enemy)
        if enemy.current_health == 45 and sorcerer.current_mana == 90:
            return True
    except Exception as e:
        return e





## Dungeon creation tests
# passed = create_dungeon_unit_tests()
# if passed == True:
#     result = "PASSED"
# else:
#     result = "FAILED"
# print(f"Dungeon creation unit test: {result}")
# if passed != True:
#     print(f"Error: {passed}")

## Room creation tests
# passed = create_room_unit_tests()
# if passed == True:
#     result = "PASSED"
# else:
#     result = "FAILED"
# print(f"Room creation unit test: {result}")
# if passed != True:
#     print(f"Error: {passed}")

## Creature creation tests
# passed = create_creature_unit_tests()
# if passed == True:
#     result = "PASSED"
# else:
#     result = "FAILED"
# print(f"Creature creation unit test: {result}")
# if passed != True:
#     print(f"Error: {passed}")

## Potion creation tests
# passed = create_potion_unit_tests()
# if passed == True:
#     result = "PASSED"
# else:
#     result = "FAILED"
# print(f"Potion creation unit test: {result}")
# if passed != True:
#     print(f"Error: {passed}")

## Potion use tests
# passed = use_potion_unit_tests()
# if passed == True:
#     result = "PASSED"
# else:
#     result = "FAILED"
# print(f"Potion use unit test: {result}")
# if passed != True:
#     print(f"Error: {passed}")

## Attack tests
# passed = attack_unit_tests()
# if passed == True:
#     result = "PASSED"
# else:
#     result = "FAILED"
# print(f"Attack unit test: {result}")
# if passed != True:
#     print(f"Error: {passed}")

