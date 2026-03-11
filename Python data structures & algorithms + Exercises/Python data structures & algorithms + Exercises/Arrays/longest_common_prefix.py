
def longest_common_prefix(strs: list[str]) -> str:
  words_len = len(strs)
  #print(strs[0]) #counts the number of words
  counter_lengths = [len(s) for s in strs]
  
  for i in range(min(counter_lengths)):
    
    current_char = strs[0][i]
    
    for s in strs:
      if s[i] != current_char:
        
        return strs[0][:i]

  return strs[0][:min(counter_lengths)]


    





if __name__ == '__main__':
  words = ["flower", "flight", "flow"]
  longest_common_prefix(words)