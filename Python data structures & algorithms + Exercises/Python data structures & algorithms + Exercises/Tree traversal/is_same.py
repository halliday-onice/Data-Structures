# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        #Para verificar se ambos são nulos, use:
        if p is None and q is None:
            return True
        if not p or not q: #um eh nulo e o outro nao
            return False

        if p.val != q.val: # tem valores diferentes pro mesmo no
            return False
        
        left_tree = self.isSameTree(p.left, q.left)
        right_tree = self.isSameTree(p.right, q.right)

        if left_tree == True and right_tree == True:
            return True
        else:
            return False