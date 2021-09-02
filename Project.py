import random 

print("Number uessing GameG")

number=random.randint(1,9)

chances=0

print("Guess a number between 1-9")

while chances<5:

    guess=int(input("enter your guess"))
    if guess == number:
        print("Congratulations you won")
        break
    elif guess < number:
        print("Your guess is too low, guess a higher number", guess)
    else:
        print("Your gues was too high, guess a number lower", guess)
    chances= chances+1
if not chances < 5:
    print("You Lose, the number is", number)

