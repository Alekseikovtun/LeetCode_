"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true

Example 2:
Input: nums = [5,4,3,2,1]
Output: false

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
"""
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True

        return False
    
solution = Solution()

assert solution.increasingTriplet([1,2,3,4,5]) == True
assert solution.increasingTriplet([5,4,3,2,1]) == False
assert solution.increasingTriplet([2,1,5,0,4,6]) == True