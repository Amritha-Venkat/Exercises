# # l = [1, 2, 3, 4, 5]
# # def permute(l):
# #     n = len(l)
# #     result = []
# #     c = n * [0]
# #
# #     result.append(l)
# #
# #     i = 0;
# #     while i < n:
# #         if c[i] < i:
# #             if i % 2 == 0:
# #                 tmp = l[0]
# #                 l[0] = l[i]
# #                 l[i] = tmp
# #
# #             else:
# #
# #                 tmp = l[c[i]]
# #                 l[c[i]] = l[i]
# #                 l[i] = tmp
# #
# #             result.append(l)
# #             c[i] += 1
# #             i = 0
# #         else:
# #             c[i] = 0
# #             i += 1
# #
# #     return result
# # print(permute(l))
#
# def subset_sum(numbers, target, partial=[]):
#     s = sum(partial)
#
#     # check if the partial sum is equals to target
#     if s == target:
#         print("sum(%s)=%s" % (partial, target))
#     if s >= target:
#         return  # if we reach the number why bother to continue
#
#     for i in range(len(numbers)):
#         n = numbers[i]
#         remaining = numbers[i+1:]
#         subset_sum(remaining, target, partial + [n])
# subset_sum([12,65,45,33,234],45)
# #combinations of length k
def combinations(n, list, combos=[]):
    # initialize combos during the first pass through
    if combos is None:
        combos = []

    if len(list) == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos
# print(combo)
#     for word in combo:
#         if combo[word] == key:
#             print("found")
# # subset_sum([3,9,8,4,5,7,10],15)
#
# #finding all the possible combinations of a string
# def all_combinations(string, combo=['']):
#     if len(string) == 0:
#         return combo
#     head, tail = string[0], string[1:]
#     combo = combo + list(map(lambda x: x + head, combo))
#     # print(combo)
#     for every_word in combo:
#         if every_word=="hot":
#             print("found")
#     return all_combinations(tail, combo)
#
#
# if __name__ == "__main__":
#     print(all_combinations('hostel'))
print(combinations(2,[1,3,67,9]))