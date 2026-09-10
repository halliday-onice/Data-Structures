#Given an array of positive integers nums and a positive 
# integer target, return the minimal length of a subarray 
# whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# Array: [2, 3, 1, 2, 4, 3]
# Target: 7 #objetivo: achar o menor pedaco continuo cuja a soma de 7 ou mais

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums: return 0
    
        res = float('inf')
        left_index = 0 #verify everybody
        total = 0

        for i in range(len(nums)): #i is my right index
            total += nums[i]
            while total >= target:
                #quantos elementos existem entre 2 indices => i - left_index + 1
                res = min(i - left_index + 1, res) #compara o tamanho atual da janela pra ver se eh o menor ate agora
                total -= nums[left_index]# Essa linha pega o valor total da sua soma e subtrai o número que está na posição do left_index no array. No nosso exemplo, o número no índice 0 era o 2. 
                #Então ele faz total = 8 - 2, e a soma cai para 6.
                left_index += 1
        return 0 if res == float('inf') else res
            
