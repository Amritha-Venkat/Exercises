# def isPalindrome(x):
#     """
#     :type x: int
#     :rtype: bool
#     """
#     y = str(x)
#     rev = ""
#     for i in y:
#         rev = i + rev
#     if rev == str(x):
#         return True
#     else:
#         return False
# print(isPalindrome(-121))

def isPalindromesigned(x):
    ans = ""
    ans1 = "-"
    a = 0
    a1 = 0
    if x >= 0:
        while x > 0:
            rem = x % 10
            x = x // 10
            ans = ans + str(rem)
        a += int(ans)
        return a
    elif x < 0:
        while abs(x) > 0:
            rem = abs(x) % 10
            x = abs(x) // 10
            ans1 = ans1 + str(rem)
        a1 += int(ans1)
        return a1
print(isPalindromesigned(-123))

