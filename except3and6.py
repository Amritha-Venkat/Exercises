def except3and6():
    for number in range(0,7):
        if number == 3 or number == 6:
            continue
        print(number, end = " ")


if __name__=='__main__':
    except3and6()