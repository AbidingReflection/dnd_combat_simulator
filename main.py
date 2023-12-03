from character import Character
from dice_roll import DiceRoll

character_data = [
    {"hit_points": 30, "ability_scores": {"STR": 14, "dex": 12, "CON": 13}},
    {"hit_points": 25, "ability_sclearcores": {"STR": 12}},
    {"hit_points": 20, "ability_scores": {"STR": 12}},
    {"hit_points": 31, "ability_scores": {"STR": 12}},
    {"hit_points": 50, "ability_scores": {"str": 14}},
]

print()  
# Create character instances and roll initiative
for data in character_data:
    try:
        character = Character(data["hit_points"], data["ability_scores"])
        character.print_summary()
    except ValueError as e:
        print(f"Error: {e}")
    print()  
