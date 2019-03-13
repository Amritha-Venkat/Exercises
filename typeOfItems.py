def typeOfItems(list):
    for item in list:
        print(type(item))

if __name__=='__main__':
    alist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    typeOfItems(alist)
