"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (t concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "AB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

class Solution():
    def greatestCommonDivisorofString(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        else:
            len_str1 = len(str1)
            len_str2 = len(str2)
            while len_str2 != 0:
                new_len_str1 = len_str2
                new_len_str2 = len_str1 % len_str2
                len_str1 = new_len_str1
                len_str2 = new_len_str2
            x = str1[:len_str1]
            return x

solution = Solution()

assert solution.greatestCommonDivisorofString("ABCABC", "ABC") == "ABC"
assert solution.greatestCommonDivisorofString("ABABAB", "AB") == "AB"
assert solution.greatestCommonDivisorofString("LEET", "CODE") == ""