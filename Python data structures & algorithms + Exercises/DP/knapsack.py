


def knapsack(values, weights, k, i = 0):

  if len(values) == i:
    return 0  
  if weights[i] > k:
    #se o item nao cabe,simplesmente ignore-o e veja o resultado para o resto dos itens.
    return knapsack(values,weights, k, i + 1)
  else: # O item cabe na mochila
    #k - wights[i] me faz perder espaco na mochila
    #segunda parte faz eu nao levar o item, mantenho o espaco k 
    return max(values[i] + knapsack(k - weights[i], k - weights[i], i + 1),
               knapsack(values, weights, k , i + 1))