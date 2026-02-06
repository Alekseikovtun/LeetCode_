"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3

Example 2:
Input: s = "aeiou", k = 2
Output: 2

Example 3:
Input: s = "leetcode", k = 3
Output: 2
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for i in range(k): #count vowels in 1st "window"
            if s[i] in vowels:
                count += 1

        max_count = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1

            max_count = max(max_count, count)

        return max_count

solution = Solution()

assert solution.maxVowels("abciiidef", 3) == 3
assert solution.maxVowels("aeiou", 2) == 2
assert solution.maxVowels("leetcode", 3) == 2