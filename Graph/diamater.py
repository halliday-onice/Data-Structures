# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def diameterOfBinaryTree(root) -> int:
  
  diameter_max = 0
  def __dfs(node):
    nonlocal diameter_max
    if node == None : return 0
    # diameter = O comprimento do maior caminho entre dois nodes em uma árvore
    l_height = __dfs(node.left)
    r_height = __dfs(node.right)

    diameter = l_height + r_height
    if diameter > diameter_max:
      diameter_max = diameter

    
    return max(l_height, r_height) + 1

  __dfs(root)





  



