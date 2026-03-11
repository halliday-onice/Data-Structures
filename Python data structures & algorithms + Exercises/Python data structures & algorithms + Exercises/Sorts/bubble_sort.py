#.indexes   0 1 2 3 4
# example: [4,2,6,5,1]
def bubble_sort(my_list):
  for i in range(len(my_list) - 1, 0, -1): #comeca em 5 vai ate zero decrementando(-1)
    for j in range(i):
      if my_list[j] > my_list[j + 1]:
        temp = my_list[j]
        my_list[j] = my_list[j + 1]
        my_list[j + 1] = temp

  return my_list


# ex:
example_list = [4,2,6,5,1, 3]

print(bubble_sort(example_list))