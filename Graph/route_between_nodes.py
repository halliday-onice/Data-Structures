from collections import defaultdict

class DirectedGraph:
  def __init__(self):
    self.graph = defaultdict(list)

  def add_vertex(self, node_u, node_v):
    """
        Adds a directed edge from node 'u' to node 'v'.
        since it is a directed graph
    """
    self.graph[node_u].append(node_v)
  
  def print_graph(self):
    for node in self.graph:
      print(f"node: {node} -> {self.graph[node]}")
  #DFS implementation
  def hasPath(self,current_node, target_node, visited = None): #basically a DFS
    #visited = [] se eu deixar o visited aqui, toda vez que ele rodasse o hasPath o 
    # conjunto de nos visitados ia ficar vazio

    if visited is None:
      visited = []

    if current_node == target_node:
      return True

  
    visited.append(current_node)
    print("Visited", visited)


    for node in self.graph[current_node]:
      if node not in visited: ## ONLY visit the neighbor if we haven't been there yet
        if self.hasPath(node, target_node, visited):
          return True
      
    return False


if __name__ == '__main__':
  g = DirectedGraph()
  g.add_vertex("A", "B")
  g.add_vertex("B", "C")
  g.add_vertex("C", "Z")
  
  g.print_graph()

  result = g.hasPath("A", "Z")

  
  print(f"\nIs there a path from A to Z? {result}")
  