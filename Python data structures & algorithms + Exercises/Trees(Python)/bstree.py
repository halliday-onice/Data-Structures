from queue import Queue
class Node:
      def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
      
      def __str__(self):
            return str(self.data)

class BinaryTree:
      def __init__(self, data = None, node = None):
            if node:
                  self.root = node
            elif data:
                  node = Node(data)
                  self.root = node
            else:
                  self.root = None

      def height(self, node = Node):
            if node is None:
                  node = self.root
            hleft = 0
            hright = 0
            if node.left:
                  hleft = self.height(node.left)
            if node.right:
                  hright = self.height(node.right)
            if hright > hleft: #significa que a subarvore dir eh maior
                  return hright + 1
            return hleft + 1
      def inorder_traversal(self, node = None):
            if node is None:
                  node = self.root
            if node.left:
                  self.inorder_traversal(node.left)
            print(node, end = ' ')
            if node.right:
                  self.inorder_traversal(node.right)
#a classe binary search tree  herda os atributos da classe BinaryTree
class BinarySearchTree(BinaryTree):
      def insert(self,value):
            parent = None
            aux = self.root

            while(aux):
                  parent = aux
                  if value < aux.data:
                        aux = aux.left
                  else:
                        aux = aux.right
                  if parent is None:
                        parent = Node(value)
                  elif value < parent.data:
                        parent.left = Node(value)
      def search(self, value, node = 0):
            if node == 0:
                  node = self.root
            if node is None or node.data == value:
                  return BinarySearchTree(node)
            if value < node.data:
                  return self.search(value, node.left)
            return self.search(value, node.right)
                  