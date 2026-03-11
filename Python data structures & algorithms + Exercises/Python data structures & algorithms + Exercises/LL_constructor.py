class Node:
      def __init__(self,value):
            self.next = None
            self.value = value

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
      #append an item at the end of the linked list
      def append_item_end(self, new_value):
            new_node = Node(new_value)
            if self.head is None:
                  self.head = new_node
                  self.tail = new_node
            else:
                  self.tail.next = new_node
                  self.tail = new_node
            self.length += 1
            return True
      #so, since it is a pop, i will not include nothing as a parameter
      def pop_item(self):


            if self.head is None and self.tail is None: #or if len == 0
                  return None
            temp = self.head # temp is the item we are going to pop out the linked list
            pred = self.head
            i = 0
            while(temp.next is not None):
                  pred = temp #this shit here is fucking amazing, assign pred first than the temp is awsome- it is a simply strategy but it works just fine, cool
                  temp = temp.next
                  print(f"iteration i: {i}, pred: {pred.value}, temp: {temp.value}")
                  i+=1
            self.tail = pred
            self.tail.next = None
            self.length -= 1
            #if we have only one item in the linked list
            if self.length == 0:
                  self.head = None
                  self.tail = None
            return temp
      
      def prepend(self, value):
            new_node = Node(value)
            if self.length == 0:
                  self.head = self.tail = new_node
            else:
                  new_node.next = self.head
                  self.head = new_node
            self.length += 1
            return True
      def pop_first_item(self):
            
            if self.length == 0:
                  print("list is empty")
                  return None
            
            aux = self.head # this one here is created in order to 
            self.head = self.head.next
            aux.next = None #here I am braking the connection between the first one and the next, that's why we need the aux reference
            self.length -= 1
            if self.length == 0:
                  self.tail = None

            return aux 

      def get(self, index):
            if index < 0 or index >= self.length:
                  print("out of index range")
                  return None
            temp = self.head
            for _ in range(index):
                  temp = temp.next
            return temp

      def set_value(self, index, new_value):
            temp = self.get(index)
            
            if temp:
                  temp.value = new_value
                  return True
            return False
            

      def insert(self, index, new_value):
            if index < 0 or index > self.length:
                  return False
            if index == 0:
                  return self.prepend(new_value)
            if index == self.length:
                  return self.append_item_end(new_value)
            #need to keep the node before the one we are inserting
            new_node = Node(new_value)
            temp = self.get(index - 1) #taking the previous one
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
      def remove(self, index):
            if index < 0 or index >= self.length:
                  return None
            if index == 0:
                  return self.pop_first_item()
            
            if index == self.length:
                  return self.pop_item
            prev = self.get(index - 1)
            temp = prev.next #the index of the node i want to remove
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

      def reverse(self): #study this one harder
            
            temp = self.head
            self.head = self.tail
            self.tail = temp

            before = None
            after = temp.next # the next item of the temp, on first iteration is the second node

            for _ in range(self.length):
                  after = temp.next
                  temp.next = before
                  before = temp
                  temp = after




            

            
if __name__ == '__main__':
    # 11->3->23->7->4
    print("+++++++++++++++++++++")
    my_ll = LinkedList(11)
    my_ll.append_item_end(3)
    my_ll.append_item_end(23)
    my_ll.append_item_end(7)
    my_ll.print_list()
    my_ll.remove(2)
    print("++++++++++++++++++++")
    my_ll.print_list()

    print("++++++++++++++++++++") #ok it is working just fine

    #for reversing a linked list
    my_ll.reverse()
    my_ll.print_list()
#     my_ll.prepend(5)
#     my_ll.print_list()
#     my_ll.pop_first_item()
#     print("++++++++++++++++++++")
#     my_ll.print_list()
#     my_ll.pop_first_item()
#     print("++++++++++++++++++++")
#     my_ll.print_list()
#     my_ll.pop_first_item()
#     my_ll.print_list()
#     my_ll.pop_first_item()
