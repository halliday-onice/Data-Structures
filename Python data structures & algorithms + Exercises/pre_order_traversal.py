
class nodeTree:
      def __init__(self, data = None):
            self.data = data
            self.left = None
            self.right = None

      def __str__(self):
            return str(self.data)
      
def new_node_tree(new_data):
      return nodeTree(new_data)
      
      
def print_preorder(node):
      if node is None:
            return
      print(node.data)
            
      print_preorder(node.left)

      print_preorder(node.right)


if __name__ == '__main__':
      root = new_node_tree(1)
      root.left = new_node_tree(2)
      root.right = new_node_tree(3)
      root.left.left = new_node_tree(4)
      root.left.right = new_node_tree(5)

      print("Pre order traversal of binary tree is \n")
      print_preorder(root)
      