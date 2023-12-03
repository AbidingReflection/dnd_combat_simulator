from dice_roll import DiceRoll

class Character:
    ABILITY_SCORES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    ABILITY_SCORE_ABBREVIATIONS = {"STR": "strength", "DEX": "dexterity", "CON": "constitution", "INT": "intelligence", "WIS": "wisdom", "CHA": "charisma"}

    def __init__(self, hit_points: int, ability_scores: dict):
        self.hit_points = hit_points
        self.load_ability_scores(ability_scores)


    def load_ability_scores(self, ability_scores: dict):
        for ability_score, value in ability_scores.items():
            full_ability_score = self.get_full_ability_score_name(ability_score)
            if full_ability_score not in self.ABILITY_SCORES:
                raise ValueError(f"Invalid ability score: {ability_score}")
            setattr(self, full_ability_score, value)  # Use the full ability score name in lowercase
        
        # Set undefined ability scores to 10
        for ability_score in self.ABILITY_SCORES:
            if not hasattr(self, ability_score):
                setattr(self, ability_score, 10)


    def get_modifier(self, ability_score):
        full_ability_score = self.get_full_ability_score_name(ability_score)
        if full_ability_score not in self.ABILITY_SCORES:
            raise ValueError(f"Invalid ability score: {ability_score}")
        
        base_stat = getattr(self, full_ability_score)
        modifier = (base_stat - 10) // 2
        return modifier


    def get_full_ability_score_name(self, ability_score):
        return self.ABILITY_SCORE_ABBREVIATIONS.get(ability_score.upper(), ability_score.lower())


    def roll_initiative(self) -> int:
        dex_mod = self.get_modifier("DEX")
        roll = DiceRoll(f"1d20+{dex_mod}")
        return roll.result["total"]


    def print_summary(self):
        print(f"Character Summary:")
        print(f"Hit Points: {self.hit_points}")
        for ability_score in self.ABILITY_SCORES:
            modifier = self.get_modifier(ability_score)
            print(f"{ability_score.capitalize()}: {getattr(self, ability_score)} (Modifier: {modifier})")
        initiative_roll = self.roll_initiative()
        print(f"Initiative Roll: {initiative_roll.result['total']}")

