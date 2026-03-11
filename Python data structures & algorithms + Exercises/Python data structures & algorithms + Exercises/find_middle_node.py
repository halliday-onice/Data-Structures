class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    def print_list(self):
            temp = self.head
            while temp is not None:
                  print(temp.value)
                  temp = temp.next
    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
            aux = self.head #this one is slow
            aux2 = self.head #this one is fast
            

            
            while(aux2 and aux2.next):
                 aux = aux.next
                 aux2 = aux2.next.next
                 
      
            return aux
             


if __name__ == '__main__':

      my_linked_list = LinkedList(1)
      my_linked_list.append(2)
      my_linked_list.append(3)
      my_linked_list.append(4)
      my_linked_list.append(5)
      my_linked_list.append(6)
      my_linked_list.print_list()

      my_linked_list.find_middle_node()

      #print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""