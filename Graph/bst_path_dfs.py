# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        def dfs_in_order_path(node, path_str):
            if not node: return
            path_str += str(node.val)
            if node.left is not None:
            
                dfs_in_order_path(node.left, path_str + "->")
            if node.left is None and node.right is None:
                path.append(path_str) #quero o caminho completo
            
            if node.right is not None:
                dfs_in_order_path(node.right, path_str + "->")
            
            return path
        return dfs_in_order_path(root, "")


