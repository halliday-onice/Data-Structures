import math

def justify_text_badness(w, page_width):
  n = len(w)
  print(n)

  dp =[0] * (n + 1) #guarda o menor custo de separar w[i: n]
  print(dp)

  split = [0] * (n + 1) #guarda o split point otimo para a linha que comeca com w[i]
  for i in range(n - 1, -1, -1): #calcula dp do fim ate o inicio (n -1 ... 0)
    dp[i] = math.inf
    total_length = -1

    #considere todas as linhas que comecam em w[i]
    for j in range(i, n):
      total_length += len(w[j]) + 1
      print("j", j)
      print("total len",total_length)

      if total_length > page_width:
        break

      badness = (page_width - total_length) ** 2

      # dp[i] - Guarda o custo mínimo (a menor badness total) para 
      # justificar todo o texto a partir da palavra i até o final (w[i:n])
      # badness: É o custo (badness) de uma única linha que estamos testando no momento.

      # Como o algoritmo roda de trás para frente, dp[j + 1] já contém o 
      # custo ótimo e já calculado para justificar todo o texto que vem depois da
      # nossa linha atual, ou seja, de w[j+1] até o fim.
      print("dp[j + 1]", dp[j + 1])
      if dp[j + 1] + badness < dp[i]:
        # significa que acabamos de encontrar 
        # uma maneira melhor de organizar o texto a partir de w[i]
        dp[i] = dp[j + 1] + badness
        split[i] =  j + 1

# --- Example Usage ---
# INPUT: Given array of words w[0 : n].
w = ["This", "is", "a", "sample", "text", "for", "the", "justification", "problem."]
page_width = 20

justified_text = justify_text_badness(w, page_width)
print(justified_text)