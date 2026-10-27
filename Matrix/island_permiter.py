# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

def island_perimeter(grid):
  rows = len(grid)
  cols = len(grid[0])

  perimeter = 0

  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1:
        perimeter += 4
      if j + 1 < cols:
        if grid[i][j] == 1 and grid[i][j + 1]== 1:
          perimeter -= 2
      if i + 1 < rows:
        if grid[i][j] == 1 and grid[i + 1][j] == 1:
          perimeter -= 2
  return perimeter

        
          