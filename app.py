print("Welcome to my game ")
value = input("Do you want to play the game: " )
if value.lower() != 'yes':
    quit()

else:
    print("Let's play the game")
    point = 0

answer = input("what does CPU stands for ")
if answer.lower() == 'central processing unit':
    print("your answer is correct")
    point += 1

else:
    print("incorrect answer")

answer = input("what does GPU stands for ")
if answer.lower() == 'graphic processing unit':
    print("your answer is correct")
    point += 1

else:
    print("incorrect answer")

answer = input("what does RAM stands for ")
if answer.lower() == 'random access memory':
    print("your answer is correct")
    point += 1

else:
    print("incorrect answer")

answer = input("what does cal stands for ")
if answer.lower() == 'calculator':
    print("your answer is correct")
    point += 1

else:
    print("incorrect answer")
print("you got " + str (point) + "  point in this game")










