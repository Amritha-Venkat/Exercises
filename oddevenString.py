def evenodd_string(word):
    even = ""
    odd =""
    for letter in range(len(word)):
        if letter % 2 == 0:
            even += word[letter]
        else:
            odd += word[letter]
    print(even,",", odd)
if __name__=='__main__':
    N = int(input())
    for i in range(N):
        word = str(input())
        evenodd_string(word)