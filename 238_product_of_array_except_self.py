"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [1] * n #answer = [1, 1, 1, 1, ..., 1]. len(answer) = n

        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
            # print(f'% {answer[i]} = {answer[i-1]} * {nums[i-1]}') here we have the product of all to the left of i

        right_product = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right_product
            # print(f'# {answer[i]} = {answer[i]} * {right_product}')
            right_product = right_product * nums[i]

        return answer



solution = Solution()

assert solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert solution.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]