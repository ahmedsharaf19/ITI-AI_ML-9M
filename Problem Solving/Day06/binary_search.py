# Problem Link : https://leetcode.com/problems/binary-search/description/
# Submission Link : https://leetcode.com/problems/binary-search/submissions/1813117696/

from typing import List

def search(nums: List[int], target: int) -> int:
    idx = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
                middle = (right  + left) // 2
                if nums[middle] == target:
                    idx = middle
                    break
                elif (nums[middle] < target):
                    left = middle + 1
                else:
                    right = middle - 1
    return idx