from random import randint

number = randint(1, 50)

twoja_liczba = None
wynik = 0
print("Podaj liczbe w przedziale 1 - 50")
while number != twoja_liczba:
    twoja_liczba = int(input("Zgadnij liczbe!"))
    wynik += 1

    if twoja_liczba == number:
        print(f"zgadles! Twoj wynik: {wynik}")
    elif twoja_liczba < number:
        print("Twoja liczba jest za mala \n")
    elif twoja_liczba > number:
        print("Twoja liczba jest za duza \n")

