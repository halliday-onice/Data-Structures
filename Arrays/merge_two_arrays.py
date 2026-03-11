
#two arrays nums1, nums2
#o array ordenado tem que ser feito in place
#primeiros m elemntos tem que ser os que serão mergeados
#os ultimos n elementos serao 0 e ignorados
          #0,1,2,3,4,5
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#m: nums1 e n:nums2
# Output: [1,2,2,3,5,6]

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
  last_num1_index = m - 1
  last_num2_index = n - 1
  
  for i in range(m + n - 1,-1, -1):
    if last_num2_index < 0: #if this happens this means that all nums2 elements are already in the right place, were already moved
      break
    if last_num1_index >= 0 and nums1[last_num1_index] > nums2[last_num2_index]:
      nums1[i] = nums1[last_num1_index]
      last_num1_index -= 1
    else:
      nums1[i] = nums2[last_num2_index]
      last_num2_index -= 1
    
  print(nums1)

  

if __name__ == '__main__':
  nums1 = [1,2,3,0,0,0] # 3 + 3 = 6
  m = 3
  nums2 = [2,5,6]
  n = 3
  merge(nums1,m,nums2,n)