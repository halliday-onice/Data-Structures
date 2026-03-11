# You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

# Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

def buy2_chocolates(prices: list, money: int)-> int:
  min_price1 = float('inf')
  min_price2 = float('inf')
  #the goal here to catch the two smallest values
  for i in prices:
    if i < min_price1:
      min_price2 = min_price1
      min_price1 = i
    elif i < min_price2:
      min_price2 = i

  two_min_values = min_price1 + min_price2

  if two_min_values <= money:
    return money - two_min_values
  
  return money
  
  
  

  
  

if __name__ == '__main__':
  prices = [3,2,3]
  money = 3
  print(buy2_chocolates(prices, money))