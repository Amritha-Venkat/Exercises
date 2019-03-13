def Fibonacci(N):
    # for number in range(N):
        if N <= 1:
            return 1
        else:
            return Fibonacci(N - 1) + Fibonacci(N - 2)


if __name__=='__main__':
    N = 50
    for i in range(50):
        print(Fibonacci(i))
