

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores)


def remove_element(nums, val)->int:
  count_k = 0
  # k elements diferent from val
  pointer_val = 0
  for i in range(len(nums)):
    if nums[i] == val:
                
      pass #se colocar o _ o revisor do leet vai reclamar, so usa o pass
    else: # se nao forem o val
                
      nums[pointer_val] = nums[i]
      count_k += 1
      pointer_val += 1
  return count_k