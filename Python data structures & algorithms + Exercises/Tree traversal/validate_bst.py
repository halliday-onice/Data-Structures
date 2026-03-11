class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)          
        traverse(self.root)
        print(results)
        return results
        
    # WRITE IS_VALID_BST METHOD HERE #
    # if the tree is built in correctly, 
    # the IN ORDER path will always 
    # climb strictly upwards         #
    #                                #
    #                                #
    #                                #
    ##################################
    def is_valid_bst(self):
        tree_list = self.dfs_in_order() # quando eu to dentro de uma classe e quero referenciar um metodo, preciso colocar o prefixo self.
        for i in range(len(tree_list) - 1):
            if tree_list[i] >= tree_list[i + 1]:
                return False
        return True


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST is valid:")
print(my_tree.is_valid_bst())

#my_tree.dfs_in_order()

"""
    EXPECTED OUTPUT:
    ----------------
    BST is valid:
    True

 """