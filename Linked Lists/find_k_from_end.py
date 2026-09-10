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
    

#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    INDENT ALL THE WAY TO THE LEFT.          #
# 
#     1 -> 2 -> 3 -> 4 -> null
#     K = 1, OUT = 4
#     K = 2, OUT = 3
#     K = 3, OUT = 2   
#     K = 4, OUT = 1
# The idea of this algorithm is to create a gap between the slow and fast pointer
# the first for loop is to create this gap and the second (while) one is to walk until the end of the list, and the slow pointer will be exactly kth node from the end
#                                       
###############################################

def find_kth_from_end(my_linked_list, k):
      fast = my_linked_list.head
      slow = my_linked_list.head
    
      
      for _ in range(k): 
            if not fast:
                 return None
            fast = fast.next
            
      while fast:
           slow = slow.next
           fast = fast.next
      return slow
      
    

        

if __name__ == '__main__':
      my_linked_list = LinkedList(1)
      my_linked_list.append(2)
      my_linked_list.append(3)
      my_linked_list.append(4)
      my_linked_list.append(5)

      find_kth_from_end(my_linked_list, 3)
      #k = 2
      #result = find_kth_from_end(my_linked_list, k)

      #print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

