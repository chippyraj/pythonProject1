import random
top_of_range = input("enter the number : ")

if top_of_range.isalpha():
    print("enter a number")
    quit()

top_of_range = int(top_of_range)

if top_of_range <= 0:
    print("enter a value greater than zero ")
    quit()

random_number = random.randint(0, top_of_range)
guess =0

while guess < 5:
    user_guess = input("enter a guess number ")

    if user_guess.isalpha():
        print("enter a number")
        continue

    user_guess = int(user_guess)

    if user_guess <= 0:
        print("enter a value greater than zero ")
        continue

    guess = + 1

    if user_guess == random_number:
        print("you got it")
        break

    elif user_guess > random_number:
        print("you are above the range")
    else:
        print("you are below the range ")

print("you got your answer in " + str(guess) + "  guess")

