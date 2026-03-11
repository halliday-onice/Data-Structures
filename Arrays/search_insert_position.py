#Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

#Input: nums = [1,3,5,6], target = 5
#Output: 2


# Input: nums = [1,3,5,6], target = 7
# Output: 4

def search_inserted_pos(nums: list, target: int):
  begin = 0
  end = len(nums) - 1
 

  while begin <= end:

    mid = (begin + end) // 2  

    if nums[mid] == target: 
      return mid
    elif nums[mid] > target:
      end = mid - 1
      
    elif nums[mid] < target:
      begin = mid + 1
  return begin

    


if __name__ == '__main__':
  nums = [1,3,5,6]
  target = 5

  search_inserted_pos(nums, target)