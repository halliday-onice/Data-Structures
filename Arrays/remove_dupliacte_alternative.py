class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #k os numeros unicos
        pointer_uniques = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                nums[pointer_uniques] = nums[i]
                pointer_uniques += 1
        return pointer_uniques