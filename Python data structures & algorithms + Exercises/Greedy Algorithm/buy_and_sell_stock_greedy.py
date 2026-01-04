

def buy_n_sell_greedy(prices: list)-> int:
  profit = 0

  # Usamos range() para gerar índices: 0, 1, 2...
  # Vamos até len(prices) - 1 para garantir que "i + 1" exista
  for i in range(len(prices) - 1):
    if prices[i] < prices[i + 1]:
      profit += prices[i + 1] - prices[i]
  return profit

if __name__ == '__main__':
  prices = [7,1,5,3,6,4]
  print(buy_n_sell_greedy(prices))