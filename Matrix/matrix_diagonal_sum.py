# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

def diagonalSum(mat: list[list[int]]) -> int:
  #secondary diagonal
  # mat[0, 2]
  # mat[1, 1]
  # mat[2, 0]
  rows = len(mat)
  cols = len(mat[0])
  primary_diagonal = 0
  secondary_diagonal = 0

  for i in range(rows):
    for j in range(cols):
      if i == j:
          primary_diagonal += mat[i][j]
      elif i + j == len(mat) - 1: #pode deixar len(mat) porque a matriz é quadrada
          secondary_diagonal+= mat[i][j]
  return primary_diagonal + secondary_diagonal