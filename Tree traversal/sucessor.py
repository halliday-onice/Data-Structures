#write an algorithm to find the next node(in order sucessor) 
# of a given node in a binary search tree. 
# You can assume that each node has a link to its parent

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    new_node.parent = temp
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    new_node.parent = temp
                    return True
                temp = temp.right
    
    def print_in_order_tree(self):
        self.__print_recursive(self.root)
        print()

    def __print_recursive(self, current_node):
        if current_node is None:
            return
        
        if current_node.left is not None:
            self.__print_recursive(current_node.left)
        print(current_node.value, end=" ")

        if current_node.right is not None:
            self.__print_recursive(current_node.right)
    
    def sucessor_node(self, actual_node):
      
      #scenario 1: has a right subtree
      if actual_node.right is not None:
        temp = actual_node.right

        while temp.left is not None:
            temp = temp.left
        
        return temp
      #scenario 2 do not have siblings to the right
      else:
            temp = actual_node.parent
            # Enquanto o pai existir E o nó atual for o filho da DIREITA...
            # nós precisamos continuar subindo!
            while temp is not None and actual_node == temp.right:
              actual_node = temp 
              temp = temp.parent
            
            return temp

                

if __name__ == '__main__':
  #[20, 10, 30, 5, 15, 25, 35, 12, 17]
  bst = BinarySearchTree()
  bst.insert(20)
  bst.insert(10)
  bst.insert(30)
  bst.insert(5)
  bst.insert(15)
  bst.insert(25)
  bst.insert(35)
  bst.insert(12)
  bst.insert(17)

  bst.print_in_order_tree()