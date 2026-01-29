"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4

Example 2:
Input: n = 25
Output: 1389537
"""

class Solution():
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        t0 = 0
        t1 = 1
        t2 = 1
        for i in range(3, n + 1):
            next_number = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = next_number
        return t2

solution = Solution()

assert solution.tribonacci(4) == 4
assert solution.tribonacci(25) == 1389537