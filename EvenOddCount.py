def EvenOddCount(list):
    even = 0
    odd = 0
    for i in range(len(list)):
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print("Even count ", even)
    print("Odd count ", odd)

if __name__=='__main__':
    alist = [1,2,3,4,5,6,7,8,9]
    EvenOddCount(alist)