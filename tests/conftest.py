from turtle import Turtle
from typing import Generator
from unittest.mock import patch

import pytest


@pytest.fixture(name="mock_turtle")
def _mock_turtle() -> Generator[None, None, None]:
    with patch.object(Turtle, "__new__", return_value=None):
        yield
