import random

class DiceRoll:
    ALLOWED_DICE = ["d4", "d6", "d8", "d10", "d12", "d20"]

    def __init__(self, dice_command: str):
        self.result = self.parse_command(dice_command)

    def parse_command(self, dice_command: str):
        parts = dice_command.split('+')
        dice_part = parts[0]
        modifier = 0

        # Check if modifier present
        if len(parts) > 1:
            try:
                modifier = int(parts[1])
            except ValueError:
                raise ValueError("Invalid modifier")

        # Split dice_part
        count, dice_type = dice_part.split('d')
        
        # Check if dice type is allowed
        if "d" + dice_type not in self.ALLOWED_DICE:
            raise ValueError(f"Invalid dice type: {dice_type}")

        # Roll the dice
        rolls = [random.randint(1, int(dice_type)) for _ in range(int(count))]
        
        total = sum(rolls) + modifier

        return {
            "command": dice_command,
            "rolls": rolls,
            "total": total
        }