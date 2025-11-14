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
        while True:
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:  # This else corresponds to (new_node.value > temp.value)
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node) #here, we append the entire node, the object node

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value) #just the .value
            #if there is a node to the left of the current node
            if current_node.left is not None:
                queue.append(current_node.left)
            #the same if there is a node on the right
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    

if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.BFS())