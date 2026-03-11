#
# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array
#Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#
#
#Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
  seen_values = {}

  for i, number in enumerate(nums):
    distance_target = target - number
    if distance_target in seen_values:
      print(seen_values, distance_target)
      
      return [seen_values[distance_target], i]
      
    seen_values[number] = i

          
      
      


if __name__ == '__main__':
  numbers =  [3,2,4]
  target = 6
  

  print(two_sum(numbers, target))