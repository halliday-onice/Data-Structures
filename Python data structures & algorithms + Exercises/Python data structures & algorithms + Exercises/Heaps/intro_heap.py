# #heaps are usefull to keep track of the heights (or the smallest value-although it's less common)
# parent_index = int(i / 2)
# left_child = 2 * parent_index
# right_child = 2 * parent_index + 1

class MaxHeap:
  def __init__(self):
    self.heap = []
  
  def __left_child(self, index):
    return 2 * index + 1
  def __right_child(self, index):
    return 2 * index + 2
  def _parent(self, index):
    return (index - 1) // 2
  
  def _swap(self, index1, index2):
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

  def insert(self, value):
    self.heap.append(value)
    current = len(self.heap) - 1 # current is just a pointer to the item we have just added
    #we only want to run this if the value at the index of current is greater than the value of parent
    while current > 0 and self.heap[current] > self.heap[self._parent(current)]: # so here basically what I am doing is going up on the heap
      self._swap(current, self._parent(current))
      current = self._parent(current)
    

  
my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)

print(my_heap.heap)

my_heap.insert(100)

print(my_heap.heap)

my_heap.insert(75)