"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        
        collected_vowels = []
        for char in s:
            if char in vowels:
                collected_vowels.append(char)
        
        reversed_vowels = collected_vowels[::-1]

        result = []
        vowel_index = 0

        for char in s:
            if char in vowels:
                result.append(reversed_vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
        
        return ''.join(result)

solution = Solution()

assert solution.reverseVowels("IceCreAm") == "AceCreIm"
assert solution.reverseVowels("leetcode") == "leotcede"