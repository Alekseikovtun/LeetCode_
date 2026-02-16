"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

solution = Solution()

assert solution.strStr(haystack = "sadbutsad", needle = "sad") == 0
assert solution.strStr(haystack = "leetcode", needle = "leeto") == -1