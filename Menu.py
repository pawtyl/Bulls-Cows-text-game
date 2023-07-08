import os
from Dictionary import Dictionary
from Validator import Validator
from Engine import Engine
from Highscores import Highscores


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Menu:
    attempt_amount = 10

    level = None
    word = None
    attempt = None
    word_length = []
    highscores = []
    words = []

    def game(self):
        self.attempt = input("Podaj wyraz: ")
        self.attempt = self.attempt.upper()
        attempt_v = Validator(self.attempt)
        if attempt_v.no_same_letters():
            attempt_e = Engine(self.attempt)
            return attempt_e.logic(self.word)

    def attempts(self):
        attempt_amount = self.attempt_amount
        while attempt_amount > 0:
            print(f"Liczba prób: {attempt_amount}. \n")
            if self.game() == len(self.word):
                print("Brawo! Udało Ci się odgadnąć wyraz!")
                self.word_length.append(str(len(self.word)))
                self.highscores.append(str(self.attempt_amount - attempt_amount + 1))
                self.words.append(self.word)
                break
            attempt_amount -= 1
        if attempt_amount <= 0:
            print(f'Niestety nie udało Ci się odgadnąć wyrazu. Poszukiwany wyraz to "{self.word.capitalize()}". ')

    def menu(self):
        print("""\nWitaj w grze Bulls & Cows!
1 - Nowa Gra
2 - Zasady Gry
3 - Zmień liczę prób
4 - Zmień poziom trudności
5 - Zapisz swoje wyniki do pliku
6 - Koniec""")
        choice = input("Podaj numer opcji, którą chcesz wybrać: ")

        if choice == "1":
            dictionary = Dictionary()
            self.word = dictionary.random_word(self.level)
            self.word = self.word.upper()
            print(f"\nZgadnij wyraz, który ma {len(self.word)} liter. ")

            self.attempts()

        elif choice == "2":
            print("""\nZasady gry:
W tekstowej grze Bulls & Cows zadaniem gracza jest odgadnięcie
wylosowanego przez komputer słowa, w którym nie powtarzają się wyrazy.
Komputer po każdej próbie wyświetla liczbę Cows & Bulls. 
Liczba przy Cows oznacza literę występującą w słowie, lecz na złej
pozycji, liczba przy Bulls pokazuje poprawną literę na poprawnej pozycji. 
Gra skończy się, gdy liczba przy Bulls będzie taka sama jak długość słowa
wylosowanego przez komputer.""")
            input("\nNaciśnij enter aby wrócić do menu. ")
            clear()

        elif choice == "3":
            try:
                self.attempt_amount = int(input("\nPodaj liczbę prób: "))
            except ValueError:
                print("Nie podałeś liczby. Pozostaje ustawienie poprzednie. ")

        elif choice == "4":
            try:
                level = int(input("""\nPodaj liczbę (zakres 3-9) liter wyrazu do zgadnięcia.
Podaj 0 aby powrócić do losowania liczb o różnej długości: """))
                if 3 <= level <= 9:
                    self.level = level
                elif level == 0:
                    self.level = None
                else:
                    print("Nie podałeś liczby z odpowiedniego zakresu. Pozostaje ustawienie poprzednie. ")
            except ValueError:
                print("Nie podałeś liczby. Pozostaje ustawienie poprzednie. ")

        elif choice == "5":
            highscore = Highscores(self.word_length, self.highscores, self.words)
            highscore.export_scores()

        elif choice == "6":
            print("\nDo widzenia!")
            exit()

        else:
            clear()
            print("Podałeś niepoprawny numer. Spróbuj jeszcze raz. ")

        self.menu()
