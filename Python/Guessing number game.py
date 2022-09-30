
print("GUESSING NUMBER GAME. . . .")
print('')
import random
while True:
    fix=random.randint(1,5)
    i=1
    while i<=3:
        guess=int(input("Enter the guessing number:"))
        if guess==fix:
            print("You won the game")
            break
        else:
            print("Wrong guess. . .")
        i+=1
    else:
        print("You lost the game. . . .")
    ch=input("Do you want to play again?(yes/no):")
    print('')
    if ch=="no":
        break
print("Game over. . . . .")




