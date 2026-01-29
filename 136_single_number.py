"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""
from typing import List

class Solution():
    def singleNumber(self, nums: List[int]) -> int:
        array_with_double_check: List[int] = []
        for i in nums:
            if i in array_with_double_check:
                array_with_double_check.remove(i)
            else:
                array_with_double_check.append(i)
        
        for i in array_with_double_check:
            need_to_return = i
        return need_to_return
    
solution = Solution()

assert solution.singleNumber([2,2,1]) == 1
assert solution.singleNumber([4,1,2,1,2]) == 4
assert solution.singleNumber([1]) == 1