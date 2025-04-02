class Node:
      def __init__(self, value):
            self.value = value
            self.next = None
            
class LinkedList:
      def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.length = 1

      def append(self, value):
            new_node = Node(value)
            if self.length == 0:
                  self.head = new_node
            else:
                  current = self.head
                  while current.next is not None:
                        current = current.next
                  current.next = new_node
            self.length += 1
    
      def print_list(self):
            if self.head is None:
                  print("empty list")
            else:
                  temp = self.head
                  values = []
            while temp is not None:
                  values.append(str(temp.value))
                  temp = temp.next
            print(" -> ".join(values))

      #   +===================================================+
      #   |                  WRITE YOUR CODE HERE             |
      #   | Description:                                      |
      #   | - This method removes all nodes with duplicate    |
      #   |   values from the linked list.                    |
      #   | - It keeps track of seen values with a set.       |
      #   | - If a value is repeated, it is skipped over by   |
      #   |   changing the 'next' pointer of the previous     |
      #   |   node, effectively removing the duplicate.       |
      #   | - The list's length is adjusted for each removed  |
      #   |   duplicate.                                      |
      #   |                                                   |
      #   | Tips:                                             |
      #   | - We maintain a 'previous' node as a reference    |
      #   |   to re-link the list when skipping duplicates.   |
      #   | - The 'current' node iterates through the list.   |
      #   | - The 'values' set holds unique items seen so far.|
      #   1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
      #   +===================================================+
      def remove_duplicates(self):
            
            temp = self.head
            prev = self.head
            seen_values_set = set()
            
            while(temp.next is not None):
                  

                  print(seen_values_set)
                  if temp.value in seen_values_set: #it is repeated
                        seen_values_set.add(temp.value) # I am creating the set but I dont know what exactly I am supposed to do with this
                        prev.next = temp.next # I am 
                  else: #if it is not repeated, add it to the set, and move the prev
                        seen_values_set.add(temp.value)
                        prev = temp
                  temp = temp.next
            


                  


            
            


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(5)
ll.remove_duplicates()
ll.print_list()

# def test_remove_duplicates(linked_list, expected_values):
#       print("Before: ", end="")
#       linked_list.print_list()
#       linked_list.remove_duplicates()
#       print("After:  ", end="")
#       linked_list.print_list()

#       # Collect values from linked list after removal
#       result_values = []
#       node = linked_list.head
#       while node:
#             result_values.append(node.value)
#             node = node.next

#       # Determine if the test passes
#       if result_values == expected_values:
#             print("Test PASS\n")
#       else:
#             print("Test FAIL\n")

#       # Test 1: List with no duplicates
#       ll = LinkedList(1)
#       ll.append(2)
#       ll.append(3)
#       test_remove_duplicates(ll, [1, 2, 3])

#       # Test 2: List with some duplicates
#       ll = LinkedList(1)
#       ll.append(2)
#       ll.append(1)
#       ll.append(3)
#       ll.append(2)
#       test_remove_duplicates(ll, [1, 2, 3])

#       # Test 3: List with all duplicates
#       ll = LinkedList(1)
#       ll.append(1)
#       ll.append(1)
#       test_remove_duplicates(ll, [1])

#       # Test 4: List with consecutive duplicates
#       ll = LinkedList(1)
#       ll.append(1)
#       ll.append(2)
#       ll.append(2)
#       ll.append(3)
#       test_remove_duplicates(ll, [1, 2, 3])

#       # Test 5: List with non-consecutive duplicates
#       ll = LinkedList(1)
#       ll.append(2)
#       ll.append(1)
#       ll.append(3)
#       ll.append(2)
#       ll.append(4)
#       test_remove_duplicates(ll, [1, 2, 3, 4])

#       # Test 6: List with duplicates at the end
#       ll = LinkedList(1)
#       ll.append(2)
#       ll.append(3)
#       ll.append(3)
#       test_remove_duplicates(ll, [1, 2, 3])

#       # Test 7: Empty list
#       ll = LinkedList(None)
#       ll.head = None  # Directly setting the head to None
#       ll.length = 0   # Adjusting the length to reflect an empty list
#       test_remove_duplicates(ll, [])
