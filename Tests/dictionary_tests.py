from Dictionary import Dictionary
dictionary = Dictionary()


# sprawdzam czy wyraz, zwracany przez funkcje losującą wyrazy, faktycznie jest wyrazem, czyli str
def test_random_word_str():
    assert isinstance(dictionary.random_word(None), str)


# sprawdzam, czy wylosowany wyraz nie zawiera w sobie znaku nowej linii,
# który został pobrany wraz z wyrazem z pliku, w razie błędu przy jego usuwaniu
def test_random_word_n():
    assert "\n" not in dictionary.random_word(3)


# sprawdzam czy wyraz, zwracany przez funkcje losującą wyrazy, pochodzi z bazy wyrazów
def test_random_word_random():
    assert dictionary.random_word(9) in dictionary.dictionary
