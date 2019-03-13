def reverseString():
    reverse = ""
    word = str(input("Enter a string"))
    for words in range(len(word)-1,-1,-1):
        # reverse = word[words] + reverse
        print(word[words], end = "")

if __name__ == '__main__':
    reverseString()