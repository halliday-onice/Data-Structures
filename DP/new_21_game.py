def new_21_game(n, k, max_pts):
 
  if k == 0:
    return 1 #garantidamente 1, ou seja, ela ganha 
    
  p = [0.0] * (n + 1)
  probs_sum = 1.0
  for i in range(1, n + 1):
    p[i]+= probs_sum / max_pts

    if i < k:
      probs_sum += p[i]
    if i >= max_pts: #alice nao pula mais pra lugar nenhum
      if (i - max_pts) < k:#descobre qual casa saiu da janela deslizante
        probs_sum -= p[i - max_pts] #retiramos a carta mais velha
  
  return sum(p[k : n + 1])
  
  