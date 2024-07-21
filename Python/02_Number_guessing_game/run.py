import random
jackpot_number = random.randint(1, 100)

guess_number = int(input("Enter your number from 1 to 100: "))
counter = 1


while guess_number != jackpot_number:
    if guess_number < jackpot_number:
        print("Guess Higher.")
    else:
        print("Guess Lower.")
    
    # repeate the guess process
    guess_number = int(input("Enter your number again from 1 to 100: "))
    counter += 1
print("You guess the number correct!")
print(f"You took {counter} attempts")
