# implementacao da busca binaria em Python
def binary_search(arr, item, begin_index = 0, end_index = None):
      if end_index is None:
            end_index = len(arr) - 1 #quero q seja um indice valido
      if begin_index <= end_index: #enquanto tiver uma sublista valida
            middle = (begin_index + end_index) // 2
            if arr[middle] == item:
                  return middle # encontrei o item e ele ta no indice do meio
            if arr[middle] < item: #preciso ir pra esquerda
                  return binary_search(arr, item, begin_index, end_index - 1)#lembrando que o item q esta no meio nao entra
            else:
                  return binary_search(arr, item, middle + 1, end_index)
      
      return None


if __name__ == "__main__":
      test = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43]
      binary_search(test,5)
      print(binary_search(test,5))
      print("*************")

       