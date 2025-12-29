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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node


            
            self.tail = new_node


        self.length += 1

    # WRITE MERGE METHOD HERE #
    #                         #
    #                         #
    #                         #
    #                         #
    ###########################
    def merge_LL(self, other_list):
        dummy = Node(0)
        current = dummy #keep track where we are in the new list, 
        
        while self.head is not None and other_list.head is not None:
            if(self.head.value < other_list.head.value):
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_list.head
                other_list.head = other_list.head.next
                    
            current = current.next
            
        if self.head is not None:
            current.next = self.head
        
        else:
            current.next = other_list.head
            self.tail = other_list.tail

        self.head = dummy.next
        self.length += other_list.length
l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge_LL(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""