def userInput():
    lines = []
    while True:
        user = input()
        if user:
            lines.append(user.upper())
        else:
            break
    for line in lines:
        userOutput(line)

def userOutput(line):
    print(line)

if __name__== '__main__':
    input("Enter your strings")
    userInput()

