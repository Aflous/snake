from dataclasses import dataclass
from turtle import Turtle

Position = tuple[int, int]


@dataclass
class Font:
    family: str
    size: int
    style: str
    color: str

    def get_font(self) -> tuple[str, int, str]:
        return self.family, self.size, self.style


class Scoreboard(Turtle):
    def __init__(self, alignment: str, font: Font, pos: Position, score_file: str) -> None:
        super().__init__()
        self.alignment = alignment
        self.font = font
        self.psoition = pos
        self.score_file = score_file
        self.score: int = 0
        self._initialize()

    def _initialize(self) -> None:
        self.hideturtle()
        self.color(self.font.color)
        self.penup()
        self.goto(*self.psoition)
        self.high_score: int = self._read_score()
        self._update_scoreboard()

    def _read_score(self) -> int:
        with open(self.score_file, mode="r", encoding="utf-8") as file:
            self.high_score = int(file.read())
        return self.high_score

    def _save_high_score(self) -> None:
        with open(self.score_file, mode="w", encoding="utf-8") as file:
            file.write(str(self.high_score))

    def _update_high_score(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()

    def reset(self) -> None:
        self._update_high_score()
        self.score = 0
        self._update_scoreboard()

    def _update_scoreboard(self) -> None:
        self.clear()
        self.goto(*self.psoition)
        font = self.font.get_font()
        score_str = f"Score: {self.score} High Score: {self.high_score}"
        self.write(score_str, True, align=self.alignment, font=font)

    def increase_score(self) -> None:
        self.score += 1
        self._update_high_score()
        self._update_scoreboard()
