from dataclasses import dataclass
from enum import Enum
from turtle import Turtle

Position = tuple[float, float]


class Direction(Enum):
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


@dataclass
class SnakeProperties:
    init_size: int
    shape: str
    color: str


@dataclass
class SnakeSettings:
    limits: Position
    pixel_size: int


class Snake:
    COLLISION_THRESHOLD: int = 15
    GAME_STEP: int = 20

    def __init__(self, properties: SnakeProperties, settings: SnakeSettings) -> None:
        self.init_size = properties.init_size
        self.shape = properties.shape
        self.color = properties.color
        self.pixel_size = settings.pixel_size
        self.x_limit, self.y_limit = settings.limits
        self._segments: list[Turtle] = []
        self._create_snake(self.init_size)

    def _create_snake(self, size: int) -> None:
        for i in range(size):
            self._add_segment((0, -i * self.pixel_size))
        self._head = self._segments[0]
        self._tail = self._segments[-1]

    def _add_segment(self, position: Position) -> None:
        new_segment = Turtle(self.shape)
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color(self.color)
        self._segments.append(new_segment)

    def grow(self) -> None:
        self._add_segment(self._tail.position())

    def reset(self) -> None:
        for seg in self._segments:
            seg.reset()
        self._segments.clear()
        self._create_snake(self.init_size)

    def collided_with_food(self, food: Turtle) -> bool:
        return self._head.distance(food) < self.COLLISION_THRESHOLD

    def collided_with_wall(self) -> bool:
        return abs(self._head.xcor()) > self.x_limit or abs(self._head.ycor()) > self.y_limit

    def collided_with_tail(self) -> bool:
        return any(self._head.distance(segment) < self.COLLISION_THRESHOLD for segment in self._segments[1:])

    def move(self) -> None:
        for seg_num in range(len(self._segments) - 1, 0, -1):
            x = self._segments[seg_num - 1].xcor()
            y = self._segments[seg_num - 1].ycor()
            self._segments[seg_num].goto(x, y)
        self._head.forward(self.GAME_STEP)

    def up(self) -> None:
        if self._head.heading() != Direction.DOWN.value:
            self._head.setheading(Direction.UP.value)

    def down(self) -> None:
        if self._head.heading() != Direction.UP.value:
            self._head.setheading(Direction.DOWN.value)

    def left(self) -> None:
        if self._head.heading() != Direction.RIGHT.value:
            self._head.setheading(Direction.LEFT.value)

    def right(self) -> None:
        if self._head.heading() != Direction.LEFT.value:
            self._head.setheading(Direction.RIGHT.value)
