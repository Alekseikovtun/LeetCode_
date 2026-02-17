"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

Example 3:
Input: s = " "
Output: true
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string: str = ""
        s = s.casefold()
        for char in s:
            if char.isalnum():
                new_string += char
        if new_string == new_string[::-1]:
            return True
        else:
            return False

solution = Solution()

assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
assert solution.isPalindrome("race a car") == False
assert solution.isPalindrome(" ") == True