#
# passo recursivo: DP = custo_celula_atual + min(cost_M(r + 1, c), cost_M(r, c+1))
#



memo = {}
def cost_M(i, j, M):
  
  rows = len(M)
  cols = len(M[0])

  #memo init
  state = (i, j)
  if state in memo:
    return memo[state]
  
  #se eu to no ultima celula da matriz inteira
  if i == rows - 1 and j == cols -1:
    return M[i][j]
  elif i == rows -1:
    return M[i][j] + cost_M(i, j + 1, M)
  elif j == cols -1:
    return M[i][j] + cost_M(i + 1, j, M)
  down = cost_M(i + 1, j, M)
  right = cost_M(i, j + 1, M)
  result = M[i][j] + min(down, right)

  memo[state] = result
  #return result


  return M[i][j] + min(cost_M(i + 1, j, M), cost_M(i, j + 1, M)) # comentar esta linha para usar a versao memoize



if __name__ == '__main__':
  M = [
    [3, 2, 12, 15, 10],
    [6, 19, 7, 11, 17],
    [8, 5, 12, 32, 21],
    [3, 20, 2, 9, 7]
  ]
  ans = cost_M(0, 0, M)

  print("-" * 30)
  print("MATRIZ:")
  for linha in M:
    print(linha)
  print("-" * 30)
  print(f"Custo Mínimo calculado: {ans}")