# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     no_duplicate_list = []
#     for i in nums:
#         if i not in no_duplicate_list:
#             no_duplicate_list.append(i)
#         else:
#             no_duplicate_list.remove(i)
#     return no_duplicate_list.pop()
# print(singleNumber([2,1,2]))
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    duplicate = []
    for i in nums:
        if i not in duplicate:
            duplicate.append(i)
        else:
            continue

    return duplicate
print(removeDuplicates( [1,1,2]))