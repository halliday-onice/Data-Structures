# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################
def first_non_repeating_char(recv_string: str):
    non_rep_dict = {}
    for i in range(len(recv_string)):
        
      if recv_string[i] in non_rep_dict:
        non_rep_dict[recv_string[i]] += 1

      else:
        non_rep_dict[recv_string[i]] = 1
    for i in recv_string:
      if non_rep_dict[i] == 1:
        return i

    return None

    

if __name__ == '__main__':

  print( first_non_repeating_char('leetcode') )

  print( first_non_repeating_char('hello') )

  print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""