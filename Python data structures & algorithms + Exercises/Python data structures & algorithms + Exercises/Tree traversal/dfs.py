
class Node:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
        
class BinarySearchTree:
  def __init__(self):
      self.root = None

  def insert(self, value):
      new_node = Node(value)
      if self.root is None:
          self.root = new_node
          return True
      
      temp = self.root
      while True:
          if new_node.value == temp.value:
              return False
          
          if new_node.value < temp.value:
              if temp.left is None:
                  temp.left = new_node
                  return True
              temp = temp.left
          else:  # This else corresponds to (new_node.value > temp.value)
              if temp.right is None:
                  temp.right = new_node
                  return True
              temp = temp.right
  
  def DFS_pre_order(self):
    results = []

    def traverse(current_node):
      results.append(current_node.value)
      if current_node.left is not None:
          traverse(current_node.left)
      if current_node.right is not None:
          traverse(current_node.right)
    traverse(self.root)
    return results

  def DFS_post_order(self):
    results = []

    def traverse(current_node):
      if current_node.left is not None:
        traverse(current_node.left)
      if current_node.right is not None:
         traverse(current_node.right)
      results.append(current_node.value)
    
    traverse(self.root)
    return results
    # [18, 27, 21, 52, 82, 76, 47]
  def DFS_in_order(self):
    #comeca de baixo, no canto inferior esquerdo - sobe - desce direita
    # esquerda - root - direita
    results = []
    def traverse(current_node):
      if current_node.left is not None:
        traverse(current_node.left)
      results.append(current_node.value)
      if current_node.right is not None:
         traverse(current_node.right)
    traverse(self.root)
    return results


if __name__ == '__main__':
  my_tree = BinarySearchTree()
  my_tree.insert(47)
  my_tree.insert(21)
  my_tree.insert(76)
  my_tree.insert(18)
  my_tree.insert(27)
  my_tree.insert(52)
  my_tree.insert(82)

  print(my_tree.DFS_pre_order())

  """
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 18, 27, 76, 52, 82]

 """