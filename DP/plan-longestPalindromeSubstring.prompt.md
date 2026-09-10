## Plan of attack for longest palindromic substring

### TL;DR
Use the center-expansion method: for each position in the string, expand outward around that position for odd-length palindromes and around the gap to the next position for even-length palindromes. Track the longest palindrome found.

### Steps
1. In `longest_palindrome_substring.py`, write a helper that expands around two indices (`left`, `right`) while the characters match.
2. Loop through each index `i` of the string.
3. For each `i`:
   - Expand around `(i, i)` for odd-length palindromes
   - Expand around `(i, i+1)` for even-length palindromes
4. Compare the lengths returned by both expansions and keep the longer result.
5. Return the best palindrome after checking all centers.

### Key idea
- The longest palindrome does not necessarily start at the middle of the string.
- The safest approach is to check every possible palindrome center, because any character or gap between characters can be the center of the longest palindrome.

### Verification
- Test: `"babad"` → `"bab"` or `"aba"`
- Test: `"cbbd"` → `"bb"`
- Test: `"a"` → `"a"`
- Test: `""` → `""`
- Edge cases: `"aaaa"`, `"abc"`

### Notes
- This gives an `O(n^2)` solution, which is fine for practice.
- If you want more speed later, you can learn Manacher’s algorithm after this works.
