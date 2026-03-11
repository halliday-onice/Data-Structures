
# Write a method called has_loop that is part of the linked list class.

# The method should be able to detect if there is a cycle or loop present in the linked list.

# You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.

# This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.


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
      
      def has_loop(self):
            fast = self.head
            slow = self.head

            while(fast is not None and fast.next is not None):
                  slow = slow.next
                  fast = fast.next.next
            
                  if(fast == slow):
                        return True
             
            return False
                
if __name__ == '__main__':        
    
    
    
      my_linked_list_1 = LinkedList(1)
      my_linked_list_1.append(2)
      my_linked_list_1.append(3)
      my_linked_list_1.append(4)
      my_linked_list_1.tail.next = my_linked_list_1.head
      ans = my_linked_list_1.has_loop()
      print(ans) # Returns True




      my_linked_list_2 = LinkedList(1)
      my_linked_list_2.append(2)
      my_linked_list_2.append(3)
      my_linked_list_2.append(4)
      ans2 = my_linked_list_2.has_loop() 


      print(ans2) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
