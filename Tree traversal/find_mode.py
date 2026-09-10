# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        count_node = {}
        def __traverse(node):
    
            if node is None:
                return []
            
            __traverse(node.left)

        
            
            count_node[node.val] = count_node.get(node.val, 0) + 1

            __traverse(node.right) 
  
        __traverse(root)
        max_freq = max(count_node.values())
        return [value for value, freq in count_node.items() if freq == max_freq]