 

class NodeTree:
      def __init__(self, data = None,):
            
            self.data = data
            self.left = None
            self.right = None
            
            
      def __str__(self):
            return str(self.data)
      
def print_inorder(node):
      #print ocorre NA ORDEM que se le: ESQ - RAIZ - DIR
      if node is None:
            return
      # percorrer o filho da esq primeiro
           
      print_inorder(node.left)
      print(node, end = ' ')  

      if node.right:
            print_inorder(node.right)

if __name__ == "__main__":
      
      root = NodeTree(10)
      root.left = NodeTree(20)
      root.right = NodeTree(30)
      root.left.left = NodeTree(40)
      root.left.right = NodeTree(50)
      root.right.left = NodeTree(60)
      root.right.right = NodeTree(70)
      root.left.left.right = NodeTree(80)
      print_inorder(root)