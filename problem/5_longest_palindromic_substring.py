"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""
"""
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    ## method-1 violence search, fail on (101/103) case : time limitation, time O(n^2)
    def sub_judge(start, end, len):
        if start > end:
            return len
        if start == end:
            return len + 1

        if s[start] == s[end]:
            return sub_judge(start + 1, end - 1, len + 2)
        else:
            return -1

    max_len = 0
    max_i = 0
    max_j = 0
    for i in range(len(s)):
        for j in reversed(range(i, len(s))):
            if j - i + 1 < max_len:  ## corp some search
                break
            else:
                if sub_judge(i, j, 0) > max_len:
                    max_len = sub_judge(i, j, 0)
                    max_i = i
                    max_j = j
        if len(s) - i - 1 <= max_len:  ## corp some search
            return s[max_i:max_j + 1]  ## corp some search

    return s[max_i:max_j + 1]