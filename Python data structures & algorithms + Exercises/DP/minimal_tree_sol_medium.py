# Define a TreeNode class to represent a node in the Binary Search Tree (BST)
class TreeNode:
    def __init__(self, value):
        self.value = value  # The value of the node
        self.left = None    # Pointer to the left child node
        self.right = None   # Pointer to the right child node


# Function to convert a sorted array to a Binary Search Tree (BST)
def sorted_array_to_bst(arr):
    if not arr:  # If the array is empty, return None
        return None
    # Call the helper function to construct the BST and return the root of the BST
    return construct_bst(arr, 0, len(arr) - 1)


# Helper function to construct the BST from the sorted array
def construct_bst(arr, start_idx, end_idx):
    if start_idx > end_idx:  # Base case: if start index is greater than end index, return None
        return None
    
    mid_idx = (start_idx + end_idx) // 2  # Calculate the middle index of the array
    node = TreeNode(arr[mid_idx])  # Create a new TreeNode with the middle element as the value
    
    # Recursively construct the left subtree using the left half of the array
    node.left = construct_bst(arr, start_idx, mid_idx - 1)
    # Recursively construct the right subtree using the right half of the array
    node.right = construct_bst(arr, mid_idx + 1, end_idx)
    
    return node  # Return the constructed node


# Helper function to print the tree using in-order traversal
def in_order_traversal(root):
    if root:  # Base case: if the node is None, return
        in_order_traversal(root.left)  # Traverse the left subtree
        print(root.value)  # Print the value of the current node
        in_order_traversal(root.right)  # Traverse the right subtree


# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7]
# Convert the sorted array to a BST and get the root of the BST
root = sorted_array_to_bst(sorted_array)
# Perform in-order traversal on the constructed BST
in_order_traversal(root)