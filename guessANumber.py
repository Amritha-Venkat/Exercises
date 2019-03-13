def guessTheNumber():
    userGuess = int(input("Guess a number between 1 to 9 "))
    if userGuess >= 0 and userGuess <= 9:
        print("Well Guessed")
    else:
        guessTheNumber()

if __name__=='__main__':
    guessTheNumber()

