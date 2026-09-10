# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
#
#
# # class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true


def path_sum(root, target_sum):
    if not root: return False
    
    
    def dfs(node, actual_sum):
        if not node: return False

        actual_sum += node.val

        if node.left is None and node.right is None:
            if actual_sum == target_sum: #poderia substituir por return actual_sum == target_sum
                return True
        
        
        if node.left is not None:
            if dfs(node.left, actual_sum): return True
        if node.right is not None:
            if dfs(node.right, actual_sum): return True
            
        return False
    
        
if __name__== '__main__':
    root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
    targetSum = 22
    path_sum(root, targetSum)