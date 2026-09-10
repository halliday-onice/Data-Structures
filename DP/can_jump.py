#You are given an integer array nums.
#  You are initially positioned at the 
# array's first index,
#  and each element in the array represents 
# your maximum jump 
# length at that position.

def can_jump(nums):
  memo = {}
  def __hop(index = 0):
    if index >= len(nums) - 1:
      return True

    if index in memo:
      return memo[index]
    jump_size = nums[index]
    
    for i in range(1, jump_size + 1):
        next_index = i + index
        if __hop(next_index)== True:
          memo[index] = True
          return True

    memo[index] = False
    return False
      


  return __hop(0)
   
if __name__ == '__main__':
  nums = [2,3,1,1,4]

  print(can_jump(nums))  
  


  