class Engine:
    stats = {"bulls": 0, "cows": 0}
    attempt = None

    def __init__(self, attempt):
        self.attempt = attempt

    def logic(self, word):
        if len(self.attempt) == len(word):
            i = 0
            while i < len(self.attempt):
                if self.attempt[i] in word:
                    if self.attempt[i] == word[i]:
                        self.stats["bulls"] += 1
                    else:
                        self.stats["cows"] += 1
                i += 1
            print(f"{self.stats['bulls']} Bulls, {self.stats['cows']} Cows")
        else:
            print("Podany wyraz ma niewłaściwą liczbę liter. ")
        bulls = self.stats["bulls"]
        self.stats["bulls"], self.stats["cows"] = 0, 0
        return bulls
