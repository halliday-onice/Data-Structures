#
# problem 27
# Given an integer array nums and an integer val, 
# remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

# k number of elements that are not equal to val
# ex: nums = [3,2,2,3] val = 3
# k = 2, retorno nums com primeiros dois elementos iguais a 2
#
def remove_elements(nums: list, val: int):
  k = 0
  for i in range(len(nums)):
    if nums[i] != val:
      nums[k] = nums[i] #sacada que me faltou-simples demais
      k+= 1
  return k
  for i in range(k,len(nums)):
    nums[i] = '_'
  print(k)
  print(nums)


if __name__ == '__main__':
  # nums = [3,2,2,3]
  # val = 3
  nums = [0,1,2,2,3,0,4,2]
  val = 2
  remove_elements(nums, val)