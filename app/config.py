from pydantic import BaseSettings


class Config(BaseSettings):
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    PIXEL_SIZE: int = 20
    GAME_TITLE: str
    GAME_SPEED: int
    BG_COLOR: str
    SNAKE_INIT_SIZE: int
    SNAKE_SHAPE: str
    SNAKE_COLOR: str
    FOOD_SHAPE: str
    FOOD_COLOR: str
    FOOD_SCALE: float
    FONT_FAMILY: str
    FONT_SIZE: int
    FONT_STYLE: str
    FONT_COLOR: str
    ALIGNMENT: str
    SCORE_FILE: str

    @property
    def X_LIMIT(self) -> int:  # noqa: N802
        return self.SCREEN_WIDTH // 2 - self.PIXEL_SIZE

    @property
    def Y_LIMIT(self) -> int:  # noqa: N802
        return self.SCREEN_HEIGHT // 2 - self.PIXEL_SIZE

    @property
    def TOP(self) -> tuple[int, int]:  # noqa: N802
        return 0, self.Y_LIMIT

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


def get_config() -> Config:
    return Config()
