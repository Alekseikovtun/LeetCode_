"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
You must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        zero_index = 0 

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1

        for i in range(zero_index, len(nums)):
            nums[i] = 0

        return nums
solution = Solution()

assert solution.moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
assert solution.moveZeroes([0]) == [0]