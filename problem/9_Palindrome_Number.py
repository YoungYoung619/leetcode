"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""

"""
9. Palindrome Number
Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    def sub_judge(start, end, string):
        if start >= end:
            return True

        if string[start] == string[end]:
            return sub_judge(start + 1, end - 1, string)
        else:
            return False

    return sub_judge(0, len(str(x)) - 1, str(x))