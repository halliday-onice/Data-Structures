

def merge(list1, list2):
  combined = []

  i = 0 #index of the first list
  j = 0 #index of the second list (we will loop trhough)
  while i < len(list1) and j < len(list2): #as long as both lists have items on it
    if list1[i] < list2[j]:
      combined.append(list1[i])
      i += 1
    else:
      combined.append(list2[j])
      j+=1

  #we gonna need two more while loops to iterate over
  # this is bc l1 may still have some items, and l2 does not
  while i < len(list1):# l1 still has items remaining
    combined.append(list1[i])
    i+= 1
  while j < len(list2):# l2 still has some items remaining
    combined.append(list2[j])
    j+=1
    
  return combined
  
#merge sort will break the list in half 
#base case: when len(list) = 1
#uses merge() to put lists together
def merge_sort(list):

  if len(list) == 1:
    return list
  mid_index = int(len(list) / 2)
  left = merge_sort(list[:mid_index]) #[comeca do inicio da lista ate mid_index - 1]
  right = merge_sort(list[mid_index:]) #[comeca do mid_index e vai ate o fim]

  return merge(left, right)


#print(merge([1,2,7,8], [3,4,5, 6]))

original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('original list', original_list)
print('sorted list', sorted_list)