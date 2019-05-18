print ("Wprowadz swoję imię: ")
while True:
    imie = input("--> ")
    if imie.isalpha():
        print("Witaj",imie)
        break
    else:
        print("Wprowadzone imię jest błędne, wprowadz imię jeszcze raz")
        continue

print ("Wprowadź nowe hasło:")
while True:
    haslo = input("--> ")
    if haslo.isalpha():
        print("Hasło musi składać się z liter i cyfr, wprowadź nowe hasło:")
        continue
    elif haslo.isdecimal():
        print("Hasło musi składać się z liter i cyfr, wprowadź nowe hasło:")
        continue
    elif haslo.isalnum():
        print("Twoje nowe hasło to:",haslo)
        break
