"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
"""
class Solution():
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        merged.append(word1[i:])
        merged.append(word2[j:])
        return ''.join(merged)
solution = Solution()

assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
assert solution.mergeAlternately("abcd", "pq") == "apbqcd"