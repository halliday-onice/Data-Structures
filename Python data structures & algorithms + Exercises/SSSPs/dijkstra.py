import heapq

class Edge:
  def __init__(self, w, start_v, target_v):
    self.w = w
    self.start_v = start_v
    self.target_v = target_v

class Node:
  def __init__(self, name):
    self.name = name
    self.visited = False
    self.previous = None
    self.neighbors = []
    self.min_distance = float('inf')

  #function to check if is less than
  def __lt__(self, other_node ):
    return self.min_distance < other_node.min_distance

  def add_edge(self,w, destination_v):
    edge = Edge(self, w, self, destination_v)
    self.neighbors.append(edge)
  
class Dijkstra:
  def __init__(self):
    self.heap = []
  
  def calculate(self, start_v ):
    start_v.min_distance = 0 # zero for the starting node
    heapq.heappush(self.heap, start_v)
    while self.heap:
      # pop element with lowest distance
      actual_v = heapq.heappop(self.heap)
      if actual_v.visited:
        continue
      # consider the neighbors
      for edge in actual_v.neighbors:
        start = edge.start_v
        target = edge.target_v
        new_distance = start.min_distance + edge.w
        if new_distance < target.min_distance:
          target.min_distance = new_distance
          target.previous = start
          #update the heap
          heapq.heappush(self.heap, target)
      actual_v.visited = True
  def get_shortest_path(self, vertex):
    print(f"the shortest path to the vertex is: {vertex.min_distance}")
    actual_vertex = vertex
    while actual_vertex is not None:
      print(actual_vertex, end="")
      actual_vertex = actual_vertex.previous