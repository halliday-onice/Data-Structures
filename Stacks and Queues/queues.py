#FIFO STANDS for first in, first out
#when We want to to put something on the line we say: enqueue, if we want to remove we say dequeue

class Node:
      def __init__(self, value):
            self.value = value
            self.next = None

class Queue:
      def __init__(self, value):
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.len = 1

      def print_queue(self):
            temp = self.first
            while temp is not None:
                  print(temp.value)
                  temp = temp.next

      def enqueue(self, value):
            new_node = Node(value)
            if self.first is None:
                  self.first = new_node
                  self.last = new_node
            else:
                  self.last.next = new_node
                  self.last = new_node

      def dequeue(self):
            if self.len == 0:
                  return None
            temp = self.first # sempre removemos do inicio em filas
            if self.len == 1:
                  self.first = None
                  self.last = None
            
            else:
                  self.first = self.first.next
                  temp.next = None
            self.len -= 1

            return temp


            
            
my_queue = Queue(2)

my_queue.enqueue(1)
my_queue.print_queue()

print(my_queue.dequeue())

my_queue.print_queue()