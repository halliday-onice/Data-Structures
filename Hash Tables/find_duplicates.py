# Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).

# Input:
# A list of integers nums.

# Output:
# A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].

# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]
# Explanation: The numbers 2 and 3 appear more than once in the input array.
 
# Input: nums = [1, 2, 3, 4, 5]
# Output: []
def find_duplicates(nums: list):
    duplicates = {}
    res = []
    for i in range(len(nums)):
        if nums[i] not in duplicates: 
            duplicates[nums[i]] = 1
        else:
            if duplicates[nums[i]] == 1:
                duplicates[nums[i]] += 1
                res.append(nums[i])
    return res
        
        



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )