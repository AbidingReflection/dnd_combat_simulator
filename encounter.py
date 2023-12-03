from typing import Dict, List
from character import Character

class Encounter:
    def __init__(self, factions: Dict[str, List[Character]]):
        self.factions = factions
        self.validate_factions()
        self.initiative_order = []
        self.generate_initiative_order()
    
    def validate_factions(self):
        pass

    def generate_initiative_order(self):
        for faction in self.factions:
            for character in self.factions[faction]:
                print(character.roll_initiative(), "\n")

factions_example = {

    "Pirates": [
        Character(21, {"STR": 12, "Dex": 8}),
        Character(12, {"INT": 11, "Dex": 8})
    ],

    "Good-guys™": [
        Character(30, {"STR": 15, "INT": 14, "Dex": 8}),
        Character(30, {"CON": 15, "Dex": 8}),
        Character(30, {"CON": 15, "Dex": 8}),
        Character(30, {"Dex": 20})
    ]
}

myEncounter = Encounter(factions_example)
