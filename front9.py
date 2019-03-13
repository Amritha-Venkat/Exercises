def array_front9(nums):
  for i in nums[0:4]:
    print(i)
    if i == 9:
      return True
      break

  return False
if __name__=='__main__':
    print(array_front9([1,2,9,3,4]))