class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Load high score from local file.
        with open(self.settings.save_path) as file_object:
            self.high_score = file_object.read()
        self.high_score = int(self.high_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        # Start Alien Invasion in an inactive stat.
        self.game_active = False
