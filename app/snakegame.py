import time
from dataclasses import dataclass

from food import Food
from scoreboard import Scoreboard
from snake import Snake


@dataclass
class GameComponents:
    snake: Snake
    food: Food
    scoreboard: Scoreboard


@dataclass
class GameSettings:
    game_speed: int


class SnakeGame:
    def __init__(self, components: GameComponents, settings: GameSettings) -> None:
        self.snake = components.snake
        self.food = components.food
        self.scoreboard = components.scoreboard
        self.game_step = 1 / settings.game_speed
        self.running = False

    def _delay(self) -> None:
        time.sleep(self.game_step)

    def _check_collision_with_food(self) -> None:
        if self.snake.collided_with_food(self.food):
            self.food.refresh()
            self.snake.grow()
            self.scoreboard.increase_score()

    def _check_collision_with_wall(self) -> None:
        if self.snake.collided_with_wall():
            self.snake.reset()
            self.scoreboard.reset()

    def _check_collision_with_tail(self) -> None:
        if self.snake.collided_with_tail():
            self.snake.reset()
            self.scoreboard.reset()

    def run(self) -> None:
        self._delay()
        self.snake.move()
        self._check_collision_with_food()
        self._check_collision_with_wall()
        self._check_collision_with_tail()
