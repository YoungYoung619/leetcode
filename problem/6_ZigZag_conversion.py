"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""

"""
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    ### find the patterns behind this problem , Time O(n)
    if not s or numRows == 1:
        return s

    ss = ''
    for i in range(numRows):
        for j in range(i, len(s), 2 * numRows - 2):
            if i == 0 or i == numRows - 1:
                ss += s[j]
                pass
            else:
                sub_index = (j // (2 * numRows - 2) + 1) * (2 * numRows - 2) - j % (2 * numRows - 2)
                ss += s[j]
                if sub_index < len(s):
                    ss += s[sub_index]
                pass
    return ss