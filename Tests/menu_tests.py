from Menu import Menu
from Engine import Engine
from unittest.mock import Mock

engine = Engine("bułka")
word = "budki"
menu = Menu()


def test_game():
    game = Mock()
    game(engine)
