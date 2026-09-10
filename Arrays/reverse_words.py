# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        words= []
        index1 = 0
        while index1 < len(s):
            #nao contar espacos em branco
            while index1 < len(s) and s[index1] == " ":
                index1 += 1
            if index1 >= len(s):
                break
            begin = index1

            while begin < len(s) and s[index1] != " ":
                index1+= 1
            
            word = s[begin:index1]
            # O PULO DO GATO: Inserir sempre na posição 0 faz com que
            # a primeira palavra vá sendo empurrada para trás!
            words.insert(0, word)
            return " ".join(words)
        
        
        

