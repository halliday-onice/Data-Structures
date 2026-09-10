class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_last_index = m - 1
        nums2_last_index = n - 1
        last = m + n - 1
        
        while nums1_last_index >= 0 and nums2_last_index >= 0:
            if nums1[ nums1_last_index] > nums2[nums2_last_index]:
                nums1[last] = nums1[nums1_last_index]
                nums1_last_index-=1
                last-=1
            else:
                nums1[last] = nums2[nums2_last_index]
                nums2_last_index -= 1
                last-=1
        # Se ainda sobrarem elementos no nums2, precisamos copiá-os.
        # (Se sobrarem no nums1, não precisamos fazer nada, pois já estão no lugar certo)
        while nums2_last_index >=0:
            nums1[last] = nums2[nums2_last_index]
            nums2_last_index -=1
            last -=1
        return nums1