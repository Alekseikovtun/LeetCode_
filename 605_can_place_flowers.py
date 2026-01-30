"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
"""
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0:
                    left_empty = True
                else:
                    if flowerbed[i - 1] == 0:
                        left_empty = True
                    else:
                        left_empty = False

                if i == len(flowerbed) - 1:
                    right_empty = True
                else:
                    if flowerbed[i + 1] == 0:
                        right_empty = True
                    else:
                        right_empty = False
                
                if left_empty == True and right_empty == True:
                    n -= 1
                    i += 2

                    if n <= 0:
                        return True
                else:
                    i += 1
            else:
                i += 2
        return False
        


solution = Solution()

assert solution.canPlaceFlowers([1,0,0,0,1], 1) == True
assert solution.canPlaceFlowers([1,0,0,0,1], 2) == False