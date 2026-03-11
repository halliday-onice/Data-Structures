
"""
A child is running up a staircase with n steps and can hop
either 1 step, 2 steps, or 3 steps at a time. Implement a method to
count how many 
possible ways the child can run up the stairs.
"""

# n = 1x + 2y + 3z
def counting_steps(i: int, n: int):

      if i > n:
            return 0
      if i == n:
            return 1
      else:
            return counting_steps(i + 1,n) + counting_steps(i + 2, n) +  counting_steps(i + 3, n)




if __name__ == '__main__':
      n = 3
      print(counting_steps(0,n))
