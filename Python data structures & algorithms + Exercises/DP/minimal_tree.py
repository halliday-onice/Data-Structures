""" 
Given a sorted(increasing) array with unique integer elements, write an algorithm to create a binary search tree
with minimal height
"""


class TreeNode:
      def __init__(self, key):
            self.left = None
            self.right = None
            self.value = key

def search(root, key):
      if root is None:
            return
      if root.value == key:
            return root
      if key < root.value:
            return search(root.left, key)
      return search(root.left, key)

#In order means: Left-root-right
def print_in_order(root):
      if root is None:
            return
      print_in_order(root.left)
      print(root.value, end = " ")
      print_in_order(root.right)
      
def minimal_tree(input_array,i,j):
      
      if i > j:
            return None
     
      middle_arr = (i + j) // 2
      
      print(f"Creating node with value: {input_array[middle_arr]} from array: {input_array}")

      root_tree = TreeNode(input_array[middle_arr])
      root_tree.left = minimal_tree(input_array, i ,middle_arr - 1)
      root_tree.right = minimal_tree(input_array,middle_arr + 1,  j)

      return root_tree


      return root_tree
      #print(f"a raiz eh {root_arr.value}")

if __name__ == '__main__':
      root = TreeNode(50)
      root.left = TreeNode(30)
      root.right = TreeNode(70)
      root.left.left = TreeNode(20)
      root.left.right = TreeNode(40)
      root.right.left = TreeNode(60)
      root.right.right = TreeNode(80)

      print_in_order(root)
      
      print("\n\n")
      input_arr = [1, 2, 3, 4, 5, 6, 7]
      arr_tree = minimal_tree(input_arr, 0, len(input_arr) - 1)
      print_in_order(arr_tree)