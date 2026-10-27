#Leetcode problem 54
# Given an m x n matrix, return all elements of the matrix in spiral order.
"""
Exemplo Visual - LeetCode 54 (Spiral Matrix)
Baseado na imagem de referência:

+---+---+---+
| 1 → 2 → 3 |  1. Primeira linha (Topo): Esquerda para Direita
+---+---+---+     ↓
| 4 → 5   6 |  2. Última coluna (Direita): Cima para Baixo
+---+---+---+     ↓
| 7 ← 8 ← 9 |  3. Última linha (Base): Direita para Esquerda
+---+---+---+  4. Primeira coluna (Esquerda): Baixo para Cima (4) e repete pro centro (5).

Caminho percorrido: 1 -> 2 -> 3 -> 6 -> 9 -> 8 -> 7 -> 4 -> 5
"""
def spiral_matrix(matrix): 
  rows = len(matrix)
  cols = len(matrix[0])

  row_up = 0
  last_column = cols - 1
  last_row = rows - 1
  first_column = 0
  results = []
  # row_up <= last_row: ainda existem linhas disponíveis.
  # first_column <= last_column: ainda existem colunas disponíveis.
  while row_up <= last_row and first_column <= last_column:
      for j in range(first_column, last_column + 1): # primeira linha, da esquerda para a direita.
          results.append(matrix[row_up][j])
      row_up += 1
      if first_column <= last_column:
            for i in range(row_up, last_row + 1): #última coluna, de cima para baixo.
              results.append(matrix[i][last_column])
            last_column -= 1
      if row_up <= last_row:
          for k in range(last_column, first_column - 1, -1): #última linha, da direita para a esquerda.
            results.append(matrix[last_row][k])
          last_row -= 1 #Se você altera o limite dentro do for, está mudando a borda que deveria permanecer fixa durante aquele percurso.
      
     
      if first_column <= last_column:
        for w in range(last_row, row_up - 1, -1): #primeira coluna, de baixo para cima.
          results.append(matrix[w][first_column])
        first_column += 1
  return results

if __name__ == '__main__':
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  spiral_matrix(matrix)

  