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
            self.length = 1

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
            self.tail = new_node
        self.length += 1
        return True

    # WRITE IS_PALINDROME METHOD HERE #
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################
      def is_palindrome(self):
            if self.length == 0:
                  return
            
            dummy = self.head
            tail_dummy = self.tail
            while dummy != tail_dummy and dummy.prev != tail_dummy: # explicacao detalhada no freeform Is palindrome DLL
                  if dummy.value != tail_dummy.value:
                       return False
                  
                  dummy = dummy.next
                  tail_dummy = tail_dummy.prev
            return True
                 

        
        




my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""

