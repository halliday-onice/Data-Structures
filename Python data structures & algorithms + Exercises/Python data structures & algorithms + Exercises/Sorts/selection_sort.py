#.indexes   0 1 2 3 4  5
# example: [4,2,6,5,1, 3]
def selection_sort(my_list):
  for i in range(len(my_list) - 1): #we only went through indexes zero through four
    min_index = i
    for j in range(i + 1,len(my_list)):
      if my_list[j] < my_list[min_index]:
        min_index = j
    if i != min_index:# se i for igual ao min index, eu ja to no minimo, entao eu nao quero rodar o resto
      temp = my_list[i]
      my_list[i] = my_list[ min_index ]
      my_list[min_index] = temp

  return my_list


