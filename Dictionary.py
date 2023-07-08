import random


class Dictionary:
    try:
        with open('dictionary.txt') as file:
            dictionary = file.readlines()
            i = 0
            while i < len(dictionary):
                dictionary[i] = dictionary[i].replace("\n", "")
                i += 1
            dictionary.sort(key=len)
    except FileNotFoundError:
        print("Nie znaleziono pliku")

    def random_word(self, level):
        word_num = random.randrange(0, len(self.dictionary))
        if level is not None:
            i = 0
            while i < len(self.dictionary):
                if len(self.dictionary[word_num]) == level:
                    break
                else:
                    word_num = random.randrange(0, len(self.dictionary))
                    i += 1
        return self.dictionary[word_num]
