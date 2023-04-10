from config import get_config
from game import Game

if __name__ == "__main__":
    config = get_config()
    game = Game(config)
    game.run()
