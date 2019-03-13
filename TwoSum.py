# indexes = []
# def twoSum(nums, target,partial = []):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#
    # total = 0
    # for i in range(len(partial)):
    #     total = total + partial[i]
    # # total = sum(partial)
    # if total == target:
    #     for index in range(len(partial)):
    #         indexes.append(index)
    #         # print(indexes)
    #     # return indexes
    # if total >= target:
    #     return 0
    # for i in range(len(nums)):
    #     n = nums[i]
    #     remaining = nums[i+1:]
    #     twoSum(remaining,target,partial + [n])
    #
    # return indexes
# print(twoSum([2,7,11,14],9))


def twoSum( nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i

print(twoSum([2,7,11,14],13))
