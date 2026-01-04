class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
      new_node = Node(value)
      if self.length == 0:
            self.head = new_node
            self.tail = new_node
      else:
            self.tail.next = new_node
            self.tail = new_node
      self.length += 1
      return True
    def reverse(self):
      temp = self.head
      self.head = self.tail
      self.tail = temp

      before = None
      after = temp.next

      #hard part

      for _ in range(self.length):
          after = temp.next
          temp.next = before #flips the arrow the other way
          #now there is a gap between temp and after
          before = temp 
          temp = after
       

    



if __name__ == '__main__':
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.print_list()
    ll.print("+++++++++++")
    ll.reverse()
    ll.print_list()