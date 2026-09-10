class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right



#Como o array já está ordenado em ordem crescente
# o elemento do meio do array será sempre a raiz ideal para manter a árvore balanceada.
#
#nums = [-10,-3,0,5,9]
def sorted_array_to_bst(self, nums: list):

  if not nums:
     return None
  
  middle = len(nums) // 2
  root_node = TreeNode(nums[middle])

  root_node.left = self.sorted_array_to_bst(nums[:middle])
  root_node.right = self.sorted_array_to_bst(nums[middle + 1:])

  return root_node


