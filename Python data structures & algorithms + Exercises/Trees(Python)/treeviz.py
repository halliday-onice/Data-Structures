import graphviz
from examples import inorder_example_tree

def preorder_traversal(tree, dot):
      # pre orderm significa que vou visitar a raiz primeiro
      # em seguida a sub-arvore a esquerda e dps a subdir

      #visita a raiz
      dot.node(str(tree.data), str(tree.data))
      if tree.left:
            preorder_traversal(tree.left, dot)
            dot.edge(str(tree.data), str(tree.left.data))
      if tree.right:
            preorder_traversal(tree.right, dot) # visita recursivamente a direita
            dot.edge(str(tree.data), str(tree.right.data))

def make_viz(tree, name):
      dot = graphviz.Digraph(comment = name)
      preorder_traversal(tree.root, dot)
      dot.render(directory='doctest-output', view=True)

if __name__ == '__main__':
      tree = inorder_example_tree()
      make_viz(tree, "expressao")