def majority(nums):
    freq = {}
    for item in nums:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    # print(freq)
    inverse = [(value, key) for key, value in freq.items()]
    return max(inverse)[1]
print(majority([3,2,3]))
