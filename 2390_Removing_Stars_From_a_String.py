"""
You are given a string s, which contains stars *.
In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"

Example 2:
Input: s = "erase*****"
Output: ""
"""
from typing import List

class Solution:
    def removeStars(self, s: str) -> str:
        new_list: List = []

        for character in s:
            if character == "*":
                new_list.pop()
            else:
                new_list.append(character)
        
        return "".join(new_list)

solution = Solution()

assert solution.removeStars("leet**cod*e") == "lecoe"
assert solution.removeStars("erase*****") == ""