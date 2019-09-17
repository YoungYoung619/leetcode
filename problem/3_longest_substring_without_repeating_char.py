"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    #         ## method-1 暴力搜索 time O(n^2)
    #         def sub_len(head_index, judge_cur_index, max_len):
    #             if judge_cur_index >= len(s) or s[judge_cur_index] in s[head_index:judge_cur_index]:
    #                 return max_len
    #             if s[judge_cur_index] not in s[head_index:judge_cur_index]:
    #                 return sub_len(head_index, judge_cur_index + 1, max_len + 1)

    #         if len(s) <= 1:
    #             return len(s)

    #         max_len = 0
    #         for i in range(len(s)):
    #             for j in range(i + 1, len(s)):
    #                 max_len = max(sub_len(i, j, 1), max_len)
    #             if max_len >= len(s)-i: ## corp some impossible search
    #                 break
    #         return max_len

    ## method-2 dynamic planning
    i = 0
    global_max = 0
    local_max = 0
    dd = {}
    for j in range(len(s)):
        if s[j] not in dd:
            dd[s[j]] = j
            local_max += 1
            global_max = max(global_max, local_max)
        else:
            local_max = j - dd[s[j]]
            last_i = i
            i = dd[s[j]] + 1
            for v in range(last_i, i):
                del dd[s[v]]
            dd[s[j]] = j

    return global_max