#medium
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

def num_islands(grid):
  rows = len(grid)
  cols = len(grid[0])
  visited_pos = set()

  def dfs(r, c): #encontrou a ilha, comeca a percorrer, a descobrir o tamanho dela
    #podemos continuar explorando a regiao conectada por "1"s?
    if 0 <= r < rows and 0 <= c < cols:#analisa o limite da matriz de ilhas e mar, so pode se houver limite
      if grid[r][c] == "1" and (r,c) not in visited_pos:
        visited_pos.add((r, c))
        dfs(r -1, c)
        dfs(r, c-1)
        dfs(r + 1, c)
        dfs(r, c + 1)

  count_islands = 0
  for i in range(rows): # esses dois fors procuram uma ilha que ainda nao foi encontrado
    for j in range(cols):
      if grid[i][j] == "1" and (i,j) not in visited_pos:#estou encontrando uma nova ilha que nao foi explorada ainda
        count_islands += 1
        dfs(i, j)
  return count_islands
