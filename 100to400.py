def even():
    flag = False
    for numbers in range(100,105):
        str_numbers = str(numbers)
        # print(str_numbers)
        for characters in str_numbers:
            if int(characters) % 2 == 0:
                flag = True
            else:
                flag = False
        if flag:
            print(str_numbers)



if __name__=='__main__':
    even()