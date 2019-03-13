def indexOfInteger(aList, key):
    for i in range(len(aList)):
        if aList[i]==key:
            return i
        else:
            indexOfInteger(aList[i+1 : len(aList)],key)

if __name__=='__main__':
    print(indexOfInteger([23,33,1,2,3],213))