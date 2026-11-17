import random

print("Hello Player !")
number_to_guess = random.randint(1, 100)
attempts = 0

while attempts < 7:
    try:
        number = int(input("Enter one number between 1 and 100 : "))
    except ValueError:
        print("Entre un nombre entier.")
        continue

    if not 1 <= number <= 100:
        print("Le nombre doit être entre 1 et 100.")
        continue

    attempts += 1
    information_summary = f"Tu as proposé {number} — essai {attempts}/7"

    if number < number_to_guess:
        if attempts < 7:
            print(f"{information_summary} — Trop petit ! Réessaie.")
    elif number > number_to_guess:
        if attempts < 7:
            print(f"{information_summary} — Trop grand ! Réessaie.")
    else:
        print(f"{information_summary} — Bravo, tu as trouvé le nombre !")
        break

if number != number_to_guess and attempts == 7:
    print(f"Désolé, tu as utilisé tes 7 essais. Le nombre était {number_to_guess}.")