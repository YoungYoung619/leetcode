"""
Copyright (c) College of Mechatronics and Control Engineering, Shenzhen University.
All rights reserved.

Description :


Author：Team Li
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def find_rest(current_sum, nums_start_index, results):
        if current_sum == 0 and len(results) == 3:
            return results

        for num in nums[nums_start_index:]:
            if len(results) < 3 and num not in results:
                results.append(num)
                current_sum += num
                if nums_start_index + 1 < len(nums):
                    answer = find_rest(current_sum, nums_start_index + 1, results)
                    if len(answer) == 3:
                        return answer
                    else:
                        n = results.pop(len(results)-1)
                        current_sum -= n
            elif len(results) >= 3:
                n = results.pop(len(results) - 1)
                current_sum -= n
                if nums_start_index + 1 < len(nums):
                    answer = find_rest(current_sum, nums_start_index + 1, results)
                    if len(answer) == 3:
                        return answer
                    else:
                        n = results.pop(len(results) - 1)
                        current_sum -= n
            else:  ## num in results
                continue

        return results

    results = find_rest(0, 0, [])
    return results

s = [-1,1,1,2,-1,-4]
print(threeSum(s))