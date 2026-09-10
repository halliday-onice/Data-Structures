
def maxSubArray(nums) -> int:
  if not nums:
    return 0
  max_sum = nums[0]
  sum_so_far = nums[0]

  max_sum_set = []
  for i in range(1, len(nums)):
    current_num = nums[i]

    sum_so_far = max(current_num, current_num + sum_so_far)
    print("max_sum_so_far", max_sum)
    #did we find a new global maximum ?
    max_sum = max(sum_so_far, max_sum)
    max_sum_set.append(max_sum)
  return max_sum

if __name__ == '__main__':
  #nums = [-2,1,-3,4,-1,2,1,-5,4]
  nums = [5,4,-1,7,8]
  print(maxSubArray(nums))