
my_list = [4,2,6,5, 1,3]
def insertion_sort(list: list):
  for i in range(1, len(list)): # starts from the second
    aux = list[i] #store the item on the left
    j = i - 1
    while aux < list[j] and j > -1:
      list[j + 1] = list[j]
      list[j] = aux
      j-= 1
  return list 

print(my_list, "before the sort")
insertion_sort(my_list)
print(my_list, "after the sort")