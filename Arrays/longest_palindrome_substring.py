


def longest_palindrome(s: str):
  if not s:
    return ""
  
  palindrome = ""

  str_original_len = len(s)
  #we need to assume that s[i] is the middle of a palindrome for both cases

  
  #treat every index i as a possible palindrome center
  # babad-> bab
  
  for i in range(len(s)):
  
    left, right = i -1, i + 1 #example for ODD(impar)- RACECAR
    while left >= 0 and right < str_original_len and s[left] == s[right]:
      
      #if the boundaries are being respected, and the condition s[left] == s[right] too. Keep moving
      left -=1
      right +=1
    current = s[left + 1: right - 1]
    if len(current) > len(palindrome):
      palindrome = current
  
    left , right = i, i + 1 #the center are the two letters
    while left >= 0 and right < str_original_len and s[left] == s[right]:
      
      left -= 1
      right += 1
    current = s[left + 1: right]
    if len(current) > len(palindrome):
      palindrome = current
        
  return palindrome



if __name__ == '__main__':
  s = "RACECAR"
  longest_palindrome(s)
