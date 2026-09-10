# WRITE FIND_PAIRS FUNCTION HERE #
#    find all numbers that are in arr1 and arr2, that sums up target                            
#                                #
#                                #
#                                #
##################################
def find_pairs(arr1, arr2, target):
    arr1_as_set = set(arr1)
    pairs = []
    for number in arr2:
        if target - number in arr1_as_set:
            pairs.append([target - number, number])
            
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""