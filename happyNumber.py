def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    n = str(n)
    # print(type(n))
    n = str(n)
    while n != '1':
        sum = 0
        for i in str(n):
            sum = sum + (int(i) * int(i))
        n = str(sum)
    return True
print(isHappy(19))

