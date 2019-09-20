"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""
"""
12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    def sub_roman(rest_num, result_str):
        if rest_num == 0:
            return result_str
        if rest_num // 1000:
            result_str += 'M'
            return sub_roman(rest_num - 1000, result_str)
        elif rest_num // 900:
            result_str += 'CM'
            return sub_roman(rest_num - 900, result_str)
        elif rest_num // 500:
            result_str += 'D'
            return sub_roman(rest_num - 500, result_str)
        elif rest_num // 400:
            result_str += 'CD'
            return sub_roman(rest_num - 400, result_str)
        elif rest_num // 100:
            result_str += 'C'
            return sub_roman(rest_num - 100, result_str)
        elif rest_num // 90:
            result_str += 'XC'
            return sub_roman(rest_num - 90, result_str)
        elif rest_num // 50:
            result_str += 'L'
            return sub_roman(rest_num - 50, result_str)
        elif rest_num // 40:
            result_str += 'XL'
            return sub_roman(rest_num - 40, result_str)
        elif rest_num // 10:
            result_str += 'X'
            return sub_roman(rest_num - 10, result_str)
        elif rest_num // 9:
            result_str += 'IX'
            return sub_roman(rest_num - 9, result_str)
        elif rest_num // 5:
            result_str += 'V'
            return sub_roman(rest_num - 5, result_str)
        elif rest_num // 4:
            result_str += 'IV'
            return sub_roman(rest_num - 4, result_str)
        elif rest_num // 1:
            result_str += 'I'
            return sub_roman(rest_num - 1, result_str)

    return sub_roman(num, '')