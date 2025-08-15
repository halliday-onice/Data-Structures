class Node:
      def __init__(self, value):
            self.value = value
            self.next = None

class Stack: #only add and remove from the top - it is called LIFO
      def __init__(self, value):
            new_node = Node(value)
            self.top = new_node
            self.height = 1

      def print_stack(self):
            temp = self.top
            while temp is not None:
                  print(temp.value)
                  temp = temp.next
      def push(self, value):
            new_node = Node(value)
            if self.height == 0:
                  self.top = new_node
            new_node.next = self.top
            self.top = new_node
            self.height += 1

      def pop(self):
            if self.height == 0:
                  return None
            print("Popin' the item")
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp


my_stack = Stack(6)
my_stack.push(3)
my_stack.push(4)
my_stack.print_stack()
my_stack.pop()

my_stack.print_stack()
