# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 + 15 = 17
        left_ptr_index = 0
        right_ptr_index = len(numbers) - 1

        while left_ptr_index < right_ptr_index:
            if numbers[left_ptr_index]  + numbers[right_ptr_index] == target:
                return [left_ptr_index + 1, right_ptr_index + 1]
            elif numbers[left_ptr_index]  + numbers[right_ptr_index] > target:
                right_ptr_index -= 1
            else: left_ptr_index += 1