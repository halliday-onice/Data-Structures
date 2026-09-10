#
#
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
#
def findShortestSubArray(nums) -> int:
        if not nums: return 0
        
        memo = {}
        first = {} #primeira posicao que um numero apareceu
        last = {} # a ultima posicao que apareceu, tem que atualizar sempre
        for i in range(len(nums)):
          if nums[i] not in memo: #se nao esta no dicionario, eu adiciono ele
              memo[nums[i]] = 1
              first[nums[i]] = i   #ou seja, eh a primeira vez que to vendo
          else:
            memo[nums[i]] += 1 #se ja esta apenas incremento
          last[nums[i]] = i
        #[print(memo[i]) for i in memo]
        max_degree = max(memo.values())
        min_size = len(nums) # tamanho grande
        for i in memo:
            if memo[i] == max_degree:
                list_size = last[i] - first[i] + 1
                if list_size < min_size:
                    min_size = list_size
        return min_size
            
        
             
             

if __name__ == '__main__':
    nums = [1,2,2,3,1]
    findShortestSubArray(nums)
