# n chips where the position of the ith chip is position[i]
# move the chips to the same position based on:
# position[i]: -> position[i] + 2 OR position[i] - 2. COST = 0
# position[i]: -> position[i] + 1 OR position[i] - 1. COST = 1

#. 0 1 2 3 4
# [2,2,2,3,3]

def min_cost_move_chips(position_list: list)-> int:
  cost_even = 0
  cost_odd = 0
  for i in position_list:
    if i % 2 == 0:
      cost_even += 1
    cost_odd += 1
  return min(cost_even, cost_odd)



pos = [1,1000000000]

print(min_cost_move_chips(pos))