my_list = [4,2,6,5, 1,3]

def rec_insertion_sort(list: list, list_size): #temp comecara na ultima posicao do vetor
  
  if list_size <= 1:
    return
  
  rec_insertion_sort(list, list_size -1)

  last_element = list[list_size - 1] #pegamos o ultimo elemento da lista com n -1 termos
  #comeco a comparar com o elemento anterior ao ultimo
  j = list_size - 2
  #Movemos elementos da sub-lista ordenada que sao maiores que last_element
  #uma posicao para direita
  while j >= 0 and list[j] > last_element:
    list[j + 1] = list[j] #desloca para a direita
    j = j - 1

  list[j + 1] = last_element
  #apos o loop, j + 1 eh a posicao correta para inserir o last_element
rec_insertion_sort(my_list, len(my_list))