# A binary search tree was created by traversing through an array from left to
#  right and inserting each element. 
# Given a BST with distinct elements, print all possible arrays that could have 
# led to this tree

# 1-2-3
#{2,1,3}, {3,2,1}
#o primeiro elemento do array sempre sera a raiz


class Node:
  def __init__(self, value):
    self.value = value 
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self,value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return True
    temp = self.root
    while(True):
      if new_node.value == temp.value:
        return False
      if new_node.value < temp.value:
        if temp.left is None:# so posso inserir se for vazio
          temp.left = new_node
          return True
        temp = temp.left

      else:
        if temp.right is None:
          temp.right = new_node
          return True
        temp = temp.right
  #[50, 20, 10]
  def sequences_bst(self,node):
    if node == None:
      return [[]]
    root = [node.value]
    #print(f"root: {root}")
    #when talking about side, we talk about the root-always the first element- the ex case 50
    left_side = self.sequences_bst(node.left)

    print(f"Looking the node: {node.value}, the left tree returned: {left_side}")

    right_side = self.sequences_bst(node.right)

    print(f"Looking the node: {node.value}, the right tree returned: {right_side}")




    return left_side
    
    


# -------------------- TESTING --------------------
if __name__ == "__main__":
    # Example: build tree from array [2, 1, 3] -> root=2, left=1, right=3
    bst = BinarySearchTree()
    for val in [50, 20,10, 60]:
        bst.insert(val)

    sequences = bst.sequences_bst(bst.root)
 
    