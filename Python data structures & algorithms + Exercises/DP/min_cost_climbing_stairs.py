
#cost = [10, 15, 20]



# How to "Think" about the Key
# You asked what you need to think about. The most critical question is: "What identifies the state I am in?"

# In this problem, the only thing that changes is the step. The cost array is always the same.

# If I ask for step 5, the answer is always the same number.

# Therefore, step is the Key to my dictionary.






def min_cost_climb_stair(cost)-> int:

  memo = {} #add the dictionary
  def _solution(step, cost):
    n = len(cost)

    minimum_cost = 0 

    if step >= n:
      return 0  

    if step in memo: #checks if it is in the dict
      return memo[step]
    # "The total price from here is the price of this step, plus the cheaper of the two next options."
    minimum_cost = cost[step] + min(_solution(step + 1,cost), _solution(step + 2,cost))
    
    memo[step] = minimum_cost # before salve put it in the dicr
    return minimum_cost
    #print(minimum_cost)

  return min(_solution(0, cost), _solution(1, cost))
  

if __name__ == '__main__':
  step = 0
  #cost = [10,15,20]
  cost = [1,100,1,1,1,100,1,1,100,1]
  print(min_cost_climb_stair(cost))
