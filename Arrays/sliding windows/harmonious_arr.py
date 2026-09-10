def findLHS(self, nums: list[int]) -> int:
      #harmonious: max_val - min_val = 1
      left_index = 0
      res = 0
      nums.sort()
      for i in range(1, len(nums)):
          #com o array ordenado a janela so eh valida se
          #nums[i] - nums[left_index] <= 1
          while nums[i] - nums[left_index] > 1: #serve pra encolher a janela deslizante
              left_index += 1
          if nums[i] - nums[left_index] == 1:
               res = max(res, i - left_index + 1)
      return res
      