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
                  current_node = self.head
                  while current_node.next is not None:
                        current_node = current_node.next
                  current_node.next = new_node
            self.length += 1 
    
      def print_list(self):
            temp = self.head
            while temp is not None:
                  print(temp.value)
                  temp = temp.next    
                  
      def make_empty(self):
            self.head = None
            self.tail = None
            self.length = 0
        
#   +===================================================+
#   |               WRITE YOUR CODE HERE                |
#   | Description:                                      |
#   | - This method partitions a linked list around a   |
#   |   value `x`.                                      |
#   | - It rearranges the nodes so that all nodes less  |
#   |   than `x` come before all nodes greater or equal |
#   |   to `x`.                                         |
#   |                                                   |
#   | Tips:                                             |
#   | - -> We use two dummy nodes, `dummy1` and `dummy2`,  |
#   |   to build two separate lists: one for elements   |
#   |   smaller than `x` and one for elements greater   |
#   |   or equal to `x`. <-                               |
#   | - `prev1` and `prev2` help us keep track of the   |
#   |   last nodes in these lists.                      |
#   | - Finally, we merge these two lists by setting    |
#   |   `prev1.next = dummy2.next`.                     |
#   | - The head of the resulting list becomes          |
#   |   `dummy1.next`.     
#     3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5      
#     Values less than 5: 3, 2, 1
#      Values greater than or equal to 5: 8, 5, 10                       |
#   +===================================================+

        
      def partition_list(self, x):
            if self.head is None:
                  return  #I actually dont know if it is this I should return
            #dummy1 is for the elements that are smaller than x, dummy is a Node
            dummy1 = Node(0)
            dummy2 = Node(0)
            prev1 = dummy1
            prev2 = dummy2
            aux = self.head
            while(aux):
                  next_node = aux.next
                  #print(f"next_node before detaching: {next_node.value if next_node else None}")  # Debugging
                  aux.next = None # # Detach the current node
                  #print(f"Processing aux: {aux.value}")
                  #print(f"aux:{aux.value}")
                  if aux.value < x:
                        prev1.next = aux
                        prev1 = aux #  ??
                        #print(f"prev1: {prev1.value}, prev1.next: {prev1.next.value if prev1.next else None}")
                  if aux.value >= x:
                        prev2.next = aux
                        prev2 = aux
                        #print(f"prev2: {prev2.value}, prev2.next: {prev2.next.value if prev2.next else None}")
                  #aux.next = None
                  aux = next_node
            prev1.next = dummy2.next
            return prev1
             
                 
                      




#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
#def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")

ll = LinkedList(3)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)

ll.partition_list(5)
ll.print_list()

# Run the test function
#test_partition_list()
      