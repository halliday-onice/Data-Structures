

def make_change(n: int):
  coins = [25, 10, 5, 1]
  if n == 0:#success case 
    return 1
  if n < 0:
    return 0
  
  ways = [0] * (n + 1)
  ways[0] = 1 #there is exactly one way to make change for 0 cents
  for i in coins:
    for amount in range(i, n + 1):
      #print("amount", amount)
      ways[amount] += ways[amount - i]
  return ways[n]



if __name__ == '__main__':
  n = 100
  print(f"Number of ways to make change for {n}:")
  print(make_change(n))