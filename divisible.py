def divisible():
    lower = 1500
    higher = 2700
    for i in range(1500, 2700):
        if i % 7 == 0 and i % 5 == 0:
            print(i)
if __name__=='__main__':
    divisible()