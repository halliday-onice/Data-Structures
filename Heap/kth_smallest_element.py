#You are given a list of numbers called nums and a number k.

#Your task is to write a function find_kth_smallest(nums, k) to find the kth 
# smallest number in the list.

# The list can contain duplicate numbers and k is guaranteed to be within 
# the range of the length of the list.

class MaxHeap:
  def __init__(self):
    self.heap = []
  
  def _left_child(self, index):
    return 2 * index + 1
  
  def _right_child(self, index):
    return 2 * index + 2
  
  def _parent(self, index):
    return (index - 1) // 2
  
  def _swap(self, index1, index2):
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
  
  def __len__(self):
    return len(self.heap)
  
  def heapify(self, index):
    if index == 0:
      return
    parent_index = self._parent(index)

    if self.heap[index] < self.heap[parent_index]:
      self._swap(index, parent_index)
      self.heapify(parent_index)
  
  def insert(self, value):
    self.heap.append(value)

    current = len(self.heap) - 1

    while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
      self._swap(current, self._parent(current))
      current = self._parent(current)
  
  def _sink_down(self, index):
    #compara o no atual com os nos filhos, para ver se eh necessario, "afundar" o valor que foi trocado
    max_index = index
    while True:
      left_index = self._left_child(index)
      right_index = self._right_child(index)

      if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
        max_index = left_index

      if(right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
        max_index = right_index
      
      if max_index != index:
        self._swap(index, max_index)
        index = max_index

      else:
        return
      
  def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()
        #salvando o valor da raiz
        max_value = self.heap[0] #estamos extraindo o maior elemento, que está na raiz
        self.heap[0] = self.heap.pop()#remove o ultimo elemento do heap e atribuimos esse ultimo elemento a posicao zero, a raiz
        self._sink_down(0)

        return max_value

def kth_smallest_element(nums, k):
  heap = MaxHeap()

  for i in nums:
    heap.insert(i)
    if len(heap) > k:
      heap.remove()
      
  return heap.remove()

if __name__ == '__main__':
  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
  nums2 = [3, 2, 1, 5, 6, 4]
  k2 = 2
  nums_sorted = [1,2,3,4,5,6]
  kth_smallest_element(nums2, k2)