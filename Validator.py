class Validator:
    attempt = None

    def __init__(self, attempt):
        self.attempt = attempt

    def no_same_letters(self):
        i, j = 0, 1
        while i < len(self.attempt):
            while j < len(self.attempt):
                if self.attempt[i] == self.attempt[j]:
                    print("W Twoim wyrazie powtarzają się litery. Podaj prawidłowy wyraz. ")
                    return False
                else:
                    j += 1
            i += 1
            j = i+1
        return True
