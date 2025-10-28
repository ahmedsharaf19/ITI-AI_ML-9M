# Problem Link : https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Submission Link : https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1812249176/

from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')
    for right in range(len(nums)):
        if (nums[right] == target):
            return 1
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    if min_length == float('inf'):
        return 0
    return min_length