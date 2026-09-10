# WRITE HAS_UNIQUE_CHARS FUNCTION HERE #
#                                      #
#                                      #
#                                      #
#                                      #
########################################
def has_unique_chars(input_str: str):
    unique_set = set()
    for i in range(len(input_str)):
        if input_str[i] in unique_set:
            return False
        else:
            unique_set.add(input_str[i])
    return True




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""