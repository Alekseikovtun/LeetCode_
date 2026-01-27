"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution():
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        if s_index == len(s):
            return True
        else:
            return False

solution = Solution()

assert solution.isSubsequence("abc", "ahbgdc") == True
assert solution.isSubsequence("axc", "ahbgdc") == False