
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right



def binary_tree_paths(root):
  if not root: return [] # caso a arvore esteja vazia
  visited = []
  def dfs(node, actual_path):
    if not node:
      return
    if actual_path:#atualiza o caminho com o valor do no atual
      actual_path += "->" + str(node.val)
    else:#se o caminho nao tem algo, coloca apenas o valor
      actual_path = str(node.val)
    #se eh um no folha
    if not node.left and not node.right:
      visited.append(actual_path)
      return
    #se nao eh um no folha
    if node.left:
      dfs(node.left, actual_path)
    if node.right:
      dfs(node.right, actual_path)
  dfs(root, "")
  return visited

if __name__ == '__main__':
  raiz = TreeNode(1)
  raiz.left = TreeNode(2)
  raiz.right = TreeNode(3)
  raiz.left.right = TreeNode(5)

  # 2. Executar a função
  caminhos = binary_tree_paths(raiz)

  # 3. Imprimir o resultado
  print("Caminhos encontrados:", caminhos)