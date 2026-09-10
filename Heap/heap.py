class MinHeap:
  def __init__(self):
    self.heap = []
  
  def __left_child(self, index):
    return 2 * index + 1
  
  def __right_child(self, index):
    return 2 * index + 2
  
  def __parent(self, index):
    return (index  - 1)// 2

  def __swap(self, index1, index2):
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
  
  def heapify(self, index):
    if index == 0: #ate chegar na raiz
      return # nao tem que subir
    
    parent_index = self.__parent(index)


    if self.heap[index] < self.heap[parent_index]:
      self.__swap(index, parent_index)
      self.heapify(parent_index)
    
  def heapify_down(self, index): #comparar com oq tem a esquerda e a direita pra ver qual eh o menor, fazer  swap e 
    size = len(self.heap)
    left = self.__left_child(index)
    right = self.__right_child(index)

    smallest = index

    if left < size and self.heap[left] < self.heap[smallest]:
      smallest = left
    
    if right < size and self.heap[right] < self.heap[smallest]:
      smallest = right

    #assim , dentro do smallest eu tenho a posicao do menor vetor

    if smallest != index: 
      self.__swap(index, smallest)
      self.heapify_down(smallest)
  
  def insert(self, value):
    self.heap.append(value)
    self.heapify(len(self.heap) - 1)
  
  def pop_min(self):
    if len(self.heap) == 0:
      raise IndexError("Heap is empty")
    if len(self.heap) == 1:
      return self.heap.pop()
    
    root = self.heap[0]
     