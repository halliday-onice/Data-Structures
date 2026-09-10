# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums: return 0
        count_increase = 1
        count_max_increase = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count_increase += 1
            else:
                
                #by doing this I am saving the maximum value
                count_max_increase = max(count_increase, count_max_increase)
                #resets the counter
                count_increase = 1

        return max(count_increase, count_max_increase)