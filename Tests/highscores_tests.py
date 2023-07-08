from Highscores import Highscores
highscores = Highscores(["5", "3"], ["3", "2"], ["kwiat", "kot"])


# sprawdzam czy podane wartości zostały poprawanie przekazane
def test_export_scores_words():
    assert highscores.words == ["kwiat", "kot"]


def test_export_scores_length():
    assert highscores.length == ["5", "3"]


def test_export_scores_attemps():
    assert highscores.attemps == ["3", "2"]
