
def remove_duplicates(nums_list: list):
  if not nums_list: return 0
  slow_counter = 0 #find the position where the next unique element should be written

  for i in range(1,len(nums_list)):
    if(nums_list[slow_counter] != nums_list[i]):#valor novo encontrado
      slow_counter += 1
      nums_list[slow_counter] = nums_list[i]
  
  return slow_counter + 1


if __name__ == '__main__':
  nums = [0,0,1,1,1,2,2,3,3,4]
  counter, nums = remove_duplicates(nums)
  print(counter, nums)