def isPalindrome(self, s: str) -> bool:
  clean_s = "".join(char.lower() for char in s if char.isalnum())

  for i in range(len(clean_s) // 2):
    if clean_s[i] != clean_s[len(clean_s) -1 -i]:
      return False
  return True