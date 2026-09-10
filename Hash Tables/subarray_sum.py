# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def subarray_sum(nums: list, target: int):
    indexes_sum = {0: -1} # Ao iniciar o seu dicionário com indexes_sum = {0: -1}, você cria uma "soma imaginária" de 0 acontecendo imediatamente antes do primeiro elemento da lista (ou seja, na posição -1).
    actual_sum = 0
    for i in range(len(nums)):
        
        actual_sum += nums[i]
        indexes_sum[actual_sum] = i
        if actual_sum - target in indexes_sum:
            return [indexes_sum[actual_sum - target] + 1, i]
    return []
            


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
