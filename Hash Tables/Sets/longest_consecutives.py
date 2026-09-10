# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#        Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

# Use sets to optimize the runtime of your solution.

# Input: An unsorted array of integers, nums.

# Output: An integer representing the length of the longest consecutive sequence in nums.                                          #
# #                                                  #
#                                                  #
#                                                  #
####################################################
def longest_consecutive_sequence(nums):
    consecutives_set = set(nums)
    longest_size = 0
    for x in nums:
        # Só começa a contar se for o início de uma sequência
        if x - 1 not in consecutives_set:
            current_num = x
            current_size = 1
            # Vai subindo os degraus
            while current_num + 1 in consecutives_set:
                current_size += 1
                current_num += 1
                # Atualiza o recorde se a sequência atual for a maior até agora
            longest_size = max(current_size, longest_size)
    return longest_size
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""