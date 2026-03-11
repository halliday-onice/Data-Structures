# You are given an array prices where prices[i] is the price of 
# a given stock on the ith day.

# You want to maximize your profit by choosing a single day 
# to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

def max_profit(prices:list[int]) -> int:
  # there is a more 'pythonic' way of doing this but let's stick to the roots
  min_price_of_all = prices[0]
  max_profit = 0
  for i in range(len(prices)):
    if prices[i] < min_price_of_all:
      min_price_of_all = prices[i]
    if (prices[i] - min_price_of_all) > max_profit:
      max_profit = prices[i] - min_price_of_all
  
  #print(max_profit, min_price_of_all)
  return max_profit
  
  
  


  



if __name__ == "__main__":
  #prices = [7,1,5,3,6,4]
  prices = [7,6,4,3,1]
  prices = [2, 10, 1, 3]
  max_profit(prices)