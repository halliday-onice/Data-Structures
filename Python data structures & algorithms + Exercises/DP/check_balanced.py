"""
Implement a function to check if a binary tree is balanced. For the purpose of this question,
a binary tree is defined
to be a tree such that heights of the two subtrees of any node never differ 
by MORE THAN ONE

"""

class NodeTree:
      def __init__(self, v):
            self.value = v
            self.left = None
            self.right = None

      def search(self, v, root):
            if root == v:
                  return root
            if v <= root:
                  return self.search(v, root.left) # quando eu coloco self.search eh como se eu chamase para o objeto que sera criado posteriormente. EH ASSSIM QUE DEVE OCORRER
            elif v > root:
                  return self.search(v, root.right)
            return None
      
      def print_in_order(self, root):
            if root is None:
                  return
            self.print_in_order(root.left)
            print(root.value, end = " ")
            self.print_in_order(root.right)
            

      def tree_high(self, root):
            left_h, right_h = 0, 0 
            if root is None:
                  return 0
           
            left_h = self.tree_high(root.left)
            
            right_h = self.tree_high(root.right)
            
            #print(f"altura esquerda {left_h}")
            #print(f"altura direita {right_h}")
            if abs(left_h - right_h) > 1:
                  return "It is not a search tree"
            return max(left_h, right_h) + 1 # o 1 do no raiz
if __name__ == "__main__":
      root = NodeTree(50)
      root.left = NodeTree(30)
      root.right = NodeTree(70)
      root.left.left = NodeTree( 20)
      root.left.right = NodeTree(40)
     

      root.print_in_order(root)
      print("\n")
      altura = root.tree_high(root)
      print(altura)

