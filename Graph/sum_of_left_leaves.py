# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumOfLeftLeaves(root) -> int:
  sum_left = 0
  def __dfs(node):
    nonlocal sum_left
    if node is None: return #base case

    if node.left is not None:
      if node.left.left is None and node.left.right is None:#se eu tiver no no folha, ai sim eu somo
        sum_left += node.left.val
      # se eu nao estiver num nó a esquerda, prossigo no dfs
      
    __dfs(node.left) 
    __dfs(node.right)
  __dfs(root)