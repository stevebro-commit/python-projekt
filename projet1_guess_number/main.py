import random

print("Hello Player , welcome to the Guess Number Game!")
number_to_guess = random.randint(1, 100) # the machine choose a number between 1 and 100
attempts = 0 # initialization of a Number of attempts

while attempts < 7:
    try:
        number = int(input("Enter one number between 1 and 100 : ")) # ask a User to choose a Number and convert it to a integer
    
    except ValueError:
        print("please enter a whole number.")
        continue # restart the loop imediatly to let the User try again

    if not 1 <= number <= 100:
        print("the number must between 1 and 100.")
        continue # restart the loop to let the user choose a valid number

    attempts += 1 
    information_summary = f"you are proposed {number} — attempts {attempts}/7"

    if number < number_to_guess:
        if attempts < 7:
            print(f"{information_summary} — Too low ! try again.")
    elif number > number_to_guess:
        if attempts < 7:
            print(f"{information_summary} — Too hight ! try again.")
    else:
        print(f"{information_summary} — , tu congratulation  you are guessed the Number!")
        break

if number != number_to_guess and attempts == 7:
    print(f"sorry, you are using all your attempts. the Number was {number_to_guess}.")