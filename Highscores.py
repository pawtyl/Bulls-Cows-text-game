class Highscores:
    length = None
    attemps = None
    words = None

    def __init__(self, length, attemps, words):
        self.length = length
        self.attemps = attemps
        self.words = words

    def export_scores(self):
        try:
            with open('highscores.txt', "a") as file:
                i = 0
                while i < len(self.length) or i < len(self.attemps):
                    file.write("Liczba liter w słowie: " + self.length[i])
                    file.write(",\tLiczba prób: " + self.attemps[i])
                    file.write(",\tSłowo: " + self.words[i].capitalize() + "\n")
                    i += 1
                print("Zapisano. ")
        except FileNotFoundError:
            print("Nie zapisano. ")
