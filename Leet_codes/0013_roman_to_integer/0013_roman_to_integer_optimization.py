"""
Given a roman numeral, convert it to an integer.
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

class Solution():
    def romanToInt(self, s: str):
        i = 0
        summ = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,  "C": 100,  "D": 500,  "M": 1000}
        while i < len(s):
            if i == len(s) - 1:
                summ += roman_dict[s[i]]
                break
            elif roman_dict[s[i + 1]] > roman_dict[s[i]]:
                summ += roman_dict[s[i + 1]] - roman_dict[s[i]]
                i = i + 2
            else:
                summ +=  roman_dict[s[i]]
                i = i + 1
        return summ

        


solution = Solution()

assert solution.romanToInt("CCLXXXIV") == 284
assert solution.romanToInt("XV") == 15
assert solution.romanToInt("XXXIV") == 34
assert solution.romanToInt("LXXXII") == 82
assert solution.romanToInt("XCIX") == 99
assert solution.romanToInt("CI") == 101
assert solution.romanToInt("MCMXCIX") == 1999
assert solution.romanToInt("MMMCCCXXXIII") == 3333