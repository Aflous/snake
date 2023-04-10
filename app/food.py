import random
from dataclasses import dataclass
from turtle import Turtle


@dataclass
class Edge:
    x: int
    y: int


class Food(Turtle):
    def __init__(self, shape: str, color: str, scale: float, edge: tuple[int, int]) -> None:
        super().__init__()
        self.edge = Edge(*edge)
        self.shape(shape)
        self.shapesize(stretch_len=scale, stretch_wid=scale)
        self.color(color)
        self.penup()
        self.refresh()

    def refresh(self) -> None:
        x = random.randint(-self.edge.x, self.edge.x)  # noqa: S311
        y = random.randint(-self.edge.y, self.edge.y)  # noqa: S311
        self.goto(x, y)
