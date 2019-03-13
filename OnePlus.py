def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    result = []
    a = ""
    for i in digits:
        a = a + str(i)
    a = str(int(a)+1)
    for i in range(len(a)):
        result.append(int(a[i]))
    return result
print(plusOne([1,9,9]))