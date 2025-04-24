class Node:
      def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
      
class DoublyLinkedList:
      def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.len = 1
      def print_list(self):
            temp = self.head
            while temp is not None:
                  print(temp.value)
                  temp = temp.next
      def append(self, value):
            new_node = Node(value)
            if self.head is None:
                  self.head = new_node
                  self.tail = new_node
            else:
                  self.tail.next = new_node
                  new_node.prev = self.tail
                  self.tail = new_node #moves tail to the last node
            self.len += 1
            return True
      def pop(self):
            if self.len == 0: #this is for zero items
                  return None
            temp = self.tail
            if self.len == 1: #this is for one item
                  self.head = None
                  self.tail = None
            else:
                  self.tail = self.tail.prev
                  self.tail.next = None
                  temp.prev = None
            self.len -= 1
            return temp
      def prepend(self, value):
            new_node = Node(value)
            if self.len == 0:
                  self.head = new_node
                  self.tail = new_node
            else:
                  new_node.next = self.head
                  self.head.prev = new_node
                  self.head = new_node
            self.len += 1
            return True
      def pop_first(self):
            #remove the first node
            if self.len == 0: #this is for zero items
                  return None
            temp = self.head
            if self.len == 1: #this is for one item
                  self.head = None
                  self.tail = None
            else:
                  self.head = self.head.next
                  self.head.prev = None
                  temp.next = None
            self.len -= 1
            return temp
      
      def get(self, index):
            if index < 0 or index >= self.len:
                  return None
            temp = self.head
            if index < self.len /2:
                  for _ in range(index):
                        temp = temp.next
            else:
                  temp = self.tail
                  for _ in range(self.len - 1, index, -1):
                        temp = temp.prev

            return temp
      def set_value(self, index, value):
            temp = self.get(index)
            if temp:
                  temp.value = value
                  return True
            return False
      def insert(self, index, value):
            if index < 0 or index > self.len:
                  return False
            if index == 0:
                  return self.prepend(value)
            if index == self.len:
                  return self.append(value)

            new_node = Node(value)
            before = self.get(index - 1)
            after = before.next #ainda nao coloquei o novo node na posicao index, por isso posso fazer isso
            #updating the pointers
            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node

            self.len += 1

            return True
      def remove(self, index):
            if index < 0 or index > self.len:
                  return None
            if index == 0:
                  return self.pop_first()
            if index == self.len - 1:
                  return self.pop()
            
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
            
            self.len -= 1

            return temp


dll = DoublyLinkedList(0)
dll.append(1)
dll.append(2)
dll.print_list()
dll.remove(1)
dll.print_list()
# dll.append(3)
# dll.append(23)
# dll.append(7)
# dll.print_list()
# print(dll.set_value(1, 4)) #troca o 3 por 4
# dll.print_list()

# print("pop first")
# dll.pop_first()
# dll.print_list()
#print("prepend")
# dll.prepend(1)
# dll.print_list()
# print("popped")
# dll.pop()
# dll.print_list()