from Validator import Validator
validate = Validator("bułka")
validate2 = Validator("kaktus")


# sprawdzam  czy funkcja, sprawdzającą czy we wprowadzonym słowie nie powtarzają się litery,
# zwraca wartość True dla poprawanych słow i wartość False dla niepoprawnych słów
def test_no_same_letters_yes():
    assert validate.no_same_letters()


def test_no_same_letters_no():
    assert not validate2.no_same_letters()
