from Engine import Engine
engine = Engine("bułka")
word = "budki"

engine2 = Engine("kwiat")
word2 = "stoik"


# sprawdzam czy po zakończeniu działania funkcji, czyli po skończonej jednej próbie odgadnięcia wyrazu,
# pola "bulls" i "cows" mają wartość 0
def test_logic_end():
    assert engine.stats["bulls"] == 0 and engine.stats["cows"] == 0


# sprawdzam czy wartość "bulls" po próbie jest prawidłowa dla podanych wyrazów
def test_logic_bulls():
    assert engine.logic(word) == 3


def test_logic_bulls_2():
    assert engine2.logic(word2) == 0
