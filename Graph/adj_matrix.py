class Graph:
  def __init__(self):
    self.adj_list = {}

  def print_g(self):
    for vertex in self.adj_list:
      print(vertex, ':', self.adj_list[vertex])

  def add_vertex(self, vertex):
    if vertex not in self.adj_list.keys():
      self.adj_list[vertex] = []
      return True
    return False

  def add_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
      self.adj_list[v1].append(v2)
      self.adj_list[v2].append(v1)
      return True
    return False

  def remove_edge(self, v1, v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
      self.adj_list[v1].remove(v2)
      self.adj_list[v2].remove(v1)
      return True
    return False

  def remove_vertex(self, vertex):
    if vertex in self.adj_list.keys():
      for v in self.adj_list[vertex]:
        self.adj_list[v].remove(vertex)
      del self.adj_list[vertex]
      return True
    return 



if __name__ == '__main__':
  my_g = Graph()
  my_g.add_vertex('A')
  my_g.add_vertex('B')
  my_g.add_vertex('C')

  my_g.add_edge('A', 'B')
  my_g.add_edge('B', 'C')
  my_g.add_edge('C', 'A')

  my_g.remove_edge('A', 'B')

  my_g.print_g()