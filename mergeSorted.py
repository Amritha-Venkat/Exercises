def merge(nums1, m, nums2, n):

    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            i+=1
            j+=1
            continue
        else:

            nums1[i] = nums2[j]
            i += 1
            j += 1

    return nums1
print(merge([1,2,3,0,0,0],6,[4,2,5],3))