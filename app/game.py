from enum import StrEnum, auto
from functools import partial
from turtle import Screen as ScreenFactory
from turtle import _Screen as Screen

from config import Config
from food import Food
from scoreboard import Font, Scoreboard
from snake import Snake, SnakeProperties, SnakeSettings
from snakegame import GameComponents, GameSettings, SnakeGame


class Direction(StrEnum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def __str__(self) -> str:
        return super().__str__().capitalize()


class Game:
    def __init__(self, config: Config) -> None:
        self.screen = self.create_screen(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.BG_COLOR, config.GAME_TITLE)
        self.running = False
        self.game = self._create_game(config)

    def _create_game(self, config: Config) -> SnakeGame:
        # create game objects
        edge = (config.X_LIMIT, config.Y_LIMIT)
        font = Font(config.FONT_FAMILY, config.FONT_SIZE, config.FONT_STYLE, config.FONT_COLOR)

        snake_properties = SnakeProperties(config.SNAKE_INIT_SIZE, config.SNAKE_SHAPE, config.SNAKE_COLOR)
        snake_settings = SnakeSettings(edge, config.PIXEL_SIZE)
        snake = Snake(snake_properties, snake_settings)

        food = Food(shape=config.FOOD_SHAPE, color=config.FOOD_COLOR, scale=config.FOOD_SCALE, edge=edge)
        scoreboard = Scoreboard(alignment=config.ALIGNMENT, font=font, pos=config.TOP, score_file=config.SCORE_FILE)

        self.bind_keys(self.screen, snake)
        # set on close event callbacks
        root = self.screen.getcanvas().winfo_toplevel()

        game_components = GameComponents(snake, food, scoreboard)
        game_settings = GameSettings(config.GAME_SPEED)
        root.protocol("WM_DELETE_WINDOW", partial(self.on_close, self.screen))

        return SnakeGame(game_components, game_settings)

    @staticmethod
    def create_screen(width: int, height: int, bg_color: str, title: str) -> Screen:
        screen = ScreenFactory()
        screen.setup(width=width, height=height)
        screen.bgcolor(bg_color)
        screen.title(title)
        screen.tracer(0)
        screen.listen()
        return screen

    @staticmethod
    def bind_keys(screen: Screen, snake: Snake) -> None:
        screen.onkey(fun=snake.up, key=Direction.UP)
        screen.onkey(fun=snake.down, key=Direction.DOWN)
        screen.onkey(fun=snake.left, key=Direction.LEFT)
        screen.onkey(fun=snake.right, key=Direction.RIGHT)

    def on_close(self, screen: Screen) -> None:
        self.running = False
        screen.getcanvas().winfo_toplevel().destroy()

    def run(self) -> None:
        self.running = True
        while self.running:
            self.game.run()
            self.screen.update()
