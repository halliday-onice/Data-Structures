# A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

# The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

# For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
# Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.


# len(cost_list) - 1 é o último índice
# -1 é o 'stop' (ele para antes do -1, ou seja, no 0)
# -1 é o 'step' (diminuir de 1 em 1)
def min_cost_buy_candies(cost_list: list)-> int:
  cost_list.sort(reverse = True)
  #o índice do loop (i) passa a representar exatamente a ordem de importância do doce
  # indice 0-> primeiro mais caro
  # indice 1-> segundo mais caro
  total_paid_cost = 0
  for i in range(len(cost_list)):
    if (i + 1) % 3 != 0: #se o indice NÃO FOR o terceiro da lista, teremos que PAGAR por ele
      total_paid_cost += cost[i]
  return total_paid_cost


if __name__ == '__main__':
  cost = [1,2,3,4,5,6,7]
  print(min_cost_buy_candies(cost))