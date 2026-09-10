def word_search(board: list[list[str]], word: str):
  

  rows = len(board)
  columns = len(board[0])

  
  visited = set()
  def dfs(r, c, letter_index):
    if letter_index == len(word):
      return True
    if (r < 0 or c < 0) or (r >= rows or c >= columns): 
      return False
    #ja visitei nessa celula? se sim, entao nao consigo formar aquela palavra
    if board[r][c] != word[letter_index]:
      return False
    if (r, c) in visited: 
      return False
    
    visited.add((r, c))
    
    res = (dfs(r - 1, c, letter_index + 1) or  # Cima
        dfs(r + 1, c, letter_index + 1) or  # Baixo
        dfs(r, c - 1, letter_index + 1) or  # Esquerda
        dfs(r, c + 1, letter_index + 1))    # Direita
      
    visited.remove((r, c))

    return res
  
  
  for i in range(rows):
    for j in range(columns):
      if board[i][j] == word[0]:
        if dfs(i, j, 0):
          return True

  return False


