def romanToInt(s):
    p = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    ans = 0;
    left = 0
    for v in s:
        if left < p[v]:
            ans = ans - 2 * left
        ans = ans + p[v]
        left = p[v]
    return ans
print(romanToInt('IX'))