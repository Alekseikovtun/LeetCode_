"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
"""
from typing import List

class Solution():
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)

        return [diff1, diff2]

solution = Solution()

assert solution.findDifference([1,2,3], [2,4,6]) == [[1,3],[4,6]]
assert solution.findDifference([1,2,3,3], [1,1,2,2]) == [[3],[]]