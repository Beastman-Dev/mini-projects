# Room properties = name, description, search_results, exits, enemies, treasure

room_0 = {
    "name": ""
    "description": "",
    "search_results": "",
    "exits": (),
    "enemies": {},
    "treasure": {}
}

room_1 = {
    "name": "Entrance Hall",
    "description": "You're in a hallway. To the North is the dungeon entrance. There are doors to the East and West. The hall is otherwise empty.",
    "search_results": "You hear gutteral voices coming from the West and faint snoring from the East."
    "exits": ("North", "East", "West"),
    "enemies": None,
    "treasure": None
}

room_2 = {
    "name": "West Dormitory"
    "description": "This appears to be a primitive dormitory, with sleeping pallets lining the walls and various articles of clothing hung from spikes in the walls. Two goblins are laying down but awake and talking with a third, who appears to be undressing for bed. All three turn toward the door as you enter and immediately scramble for weapons.",
    "search_results": "The articles of clothing are tattered and worthless. You find five copper coins stashed in the sleeping pallets.",
    "exits": ("East", "South"),
    "enemies": {"goblins": 3},
    "treasure": {"copper": 5}
}

room_3 = {
    "name": "East Dormitory"
    "description": "This appears to be a primitive dormitory, with sleeping pallets lining the walls and various articles of clothing hung from spikes in the walls. Three goblins lay sleeping on their pallets, one snoring loudly.",
    "search_results": "The articles of clothing are tattered and worthless. You find five copper coins stashed in the sleeping pallets.",
    "exits": ("West", "South"),
    "enemies": {"goblins": 3},
    "treasure": {"copper": 5}
}

room_4 = {
    "name": ""
    "description": "",
    "search_results": "",
    "exits": (),
    "enemies": {},
    "treasure": {}
}

room_5 = {
    "name": ""
    "description": "",
    "search_results": "",
    "exits": (),
    "enemies": {},
    "treasure": {}
}

room_6 = {
    "name": ""
    "description": "",
    "search_results": "",
    "exits": (),
    "enemies": {},
    "treasure": {}
}

r1_description = ""
r1_contents = ""
