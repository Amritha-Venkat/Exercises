def digitsAndLetters(userInput):
    countOfAlpha = 0
    countOfDigits = 0
    for character in userInput:
        if character.isalpha():
            countOfAlpha += 1
        if character.isdigit():
            countOfDigits += 1
    print("Number of alphabets are ",countOfAlpha)
    print("Number of digits are",countOfDigits)
if __name__=='__main__':
    userInput = str(input("Enter your string"))
    digitsAndLetters(userInput)
