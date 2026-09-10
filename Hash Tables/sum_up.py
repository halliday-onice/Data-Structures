# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################
def two_sum(nums: list, target:int):
    sum_up = {}
    for i in range(len(nums)):
        if target - nums[i] in sum_up : #busca se o numero que falta esta no dicionario
            return [sum_up[target - nums[i]], i]
        sum_up[nums[i]] = i # Dessa forma, o dicionário vai saber rapidamente se um número já foi visto (usando a chave) e em qual posição ele estava na lista (usando o valor)
    return []
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""

