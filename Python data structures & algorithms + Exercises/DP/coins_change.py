# 15 - 2 = 13
#  minimal_coins = min(inf, 1 + coin_step(13, [2,3,7]))
#  13 - 2 = 11
#   minimal_coins = min(inf, 1 + coin_step(9, [2,3,7]))
#     9 - 2 = 7
#       minimal_coins = min(inf, 1 +coin_step(7, [2,3,7]))
#       7 - 2 = 5
#         minimal_coins = min(inf, 1 + coin_step(5, [2,3,7]))
#        5 - 2 = 3 
#           minimal_coins = min(inf, 1 + coin_step(3, [2,3,7]))
#          3 - 2 = 1
#               minimal_coins = min(inf, 1 + coin_step(1, [2,3,7]))
# 
# 

# 

def coins_step(money_amount: int, coins:list):
  if money_amount == 0: #condicao de parada
        return 0
  minimal_coins = float('inf')
  for i in coins:  
    if(money_amount - i >= 0):
      
      minimal_coins = min( minimal_coins, 1 + coins_step(money_amount - i, coins))
  print("minimal coins", minimal_coins)
  return minimal_coins

  


coins_step(15, [2, 3, 7])