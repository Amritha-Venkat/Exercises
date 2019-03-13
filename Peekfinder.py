# import random
aList=[11,3,1,1,22]

def recursiveBinarySearch(start,end,aList):
    midpt=(start+end)//2
    if(start<=end):
        if(aList[midpt]<aList[midpt-1]):
            recursiveBinarySearch(start,midpt-1,aList)
        elif(aList[midpt]<aList[midpt+1]):
            recursiveBinarySearch(midpt+1,end,aList)
        else:
            print("peak is", aList[midpt])
if __name__=='__main__':
    recursiveBinarySearch(0,4, aList)

