
class GameStats:

    def __init__(self, FlappyBirdGame):
        self.settings = FlappyBirdGame.game_settings

        self.reset_game_stat()

    def reset_game_stat(self):
        self.bird_left =self.settings.bird_life
