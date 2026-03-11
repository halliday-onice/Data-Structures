class Heap:
  def __init__(self):
    self.heap = []

  def __left_child(self, i):
    return 2 * i + 1
  def __right_child(self, i):
    return 2 * i + 2
  def __parent(self, i):
    return (i - 1) // 2
  
  def __swap(self, index1, index2):
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

  def max_heapify(self, A,i):
    l = self.__left_child(i)
    r = self.__right_child(i)
    if(A[l] > A[i] ):
      largest = l
    else:
      largest = i
    
    if(A[r] > A[largest]):
      largest = r
    
    if largest != i:
      self.__swap(A[i], A[largest])
      self.max_heapify(A, largest)

  def build_max_heap(self, A):
    self.heap = A
    heap_size = len(self.heap)
    start_index = (heap_size // 2) - 1 # In a heap, any element at an index greater than (n // 2) - 1 is a leaf.
    for i in range(start_index, -1, -1):
      self.max_heapify(A, heap_size)
  def heapsort(self, A):
    self.build_max_heap(A)
    heap_size = len(A)
    for i in range(heap_size - 1, 0 , -1):
      self.__swap(0, i)
      self.max_heapify(0, i)
      
if __name__ == "__main__":
    my_array = [4, 10, 3, 5, 1, 8]
    
    heap_obj = Heap()
    print(f"Original array: {my_array}")
    
    heap_obj.heapsort(my_array)
    
    print(f"Sorted array:   {heap_obj.heap}")
    # Expected output: [1, 3, 4, 5, 8, 10]

