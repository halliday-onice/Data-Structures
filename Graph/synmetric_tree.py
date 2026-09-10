# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Given the root of a binary tree, 
# check whether it is a mirror of itself (i.e., symmetric around its center).


def is_simmetric(root) -> bool:
    
  def __dfs(node_left, node_right):
   if node_left is None and node_right is None: return True
   if node_left is None or node_right is None: return False
   if node_left.val != node_right.val: return False
    #so consigo usar o and porque eh um problema booleano
   return __dfs(node_left.left, node_right.right) and __dfs(node_left.right, node_right.left)
  if not root: return True
  return __dfs(root.left, root.right)
     