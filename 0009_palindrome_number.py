"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1
"""
class Solution():
    def isPalindrome(self, x: int):
        base_x = x
        reverse_x = 0
        while(x > 0):
            last_item = x % 10
            reverse_x = reverse_x * 10 + last_item
            x = x // 10

        if (base_x == reverse_x):
            return True
        else:
            return False


solution = Solution()

assert solution.isPalindrome(121) == True
assert solution.isPalindrome(-121) == False
assert solution.isPalindrome(10) == False
assert solution.isPalindrome(15784048751) == True
assert solution.isPalindrome(1578448751) == True
assert solution.isPalindrome(15784487510) == False