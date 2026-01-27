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
        roman_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90,  "C": 100, "CD": 400,  "D": 500, "CM": 900,  "M": 1000}
        while i < len(s):
            try: 
                temp_1 = s[i]
                temp_2 = s[i + 1]

                count_for_summ = 0

                temp_int_1 = roman_dict[temp_1]
                temp_int_2 = roman_dict[temp_2]
                if temp_int_2 > temp_int_1:
                    temp_3 = temp_1 + temp_2
                    temp_int_3 = roman_dict[temp_3]

                    count_for_summ = temp_int_3
                    i = i + 2
                else:
                    count_for_summ = temp_int_1
                    i = i + 1
                summ = summ + count_for_summ
            except:
                last_temp = s[i]
                last_temp_int = roman_dict[last_temp]
                summ = summ + last_temp_int
                break
            if i >= len(s):
                break
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