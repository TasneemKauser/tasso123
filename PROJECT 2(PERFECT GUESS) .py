import random
randNumber=random.randint(1,10)
# print(randNumber)
userGuess=None
guessses=0
while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess:"))
    guessses+=1
    if (userGuess==randNumber):
         print("You guessed it right.")

    else: 

        if (userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number.")
        else:
            print("You guessed it wrong! Enter a larger number.")
print(f"You guessed the number in {guessses} guesses.")


with open("HhIGHSCORE.txt","r") as f:
    highscore=int(f.read())

if (guessses<highscore):
    print("you have just broken the high score.")
    with open("HhIGHSCORE.txt","w") as f:
        f.write(str(guessses))