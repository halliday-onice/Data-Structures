# WRITE FIND_LONGEST_STRING FUNCTION HERE #
#                                         #
#                                         #
#                                         #
#                                         #
###########################################
def find_longest_string(string_list):
    if not string_list: return ''
    
    max_counter = 0
    
    counter = 0
    longest_str = ""
    for i in string_list:
        
        if len(i) > max_counter:
            counter = len(i)
            max_counter = max(counter, max_counter)
            longest_str = i
    return longest_str
        
        
    


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""