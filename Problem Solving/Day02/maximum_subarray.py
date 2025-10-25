# Problem Link: https://leetcode.com/problems/maximum-subarray/
# Submission Link: https://leetcode.com/problems/maximum-subarray/submissions/1809176673/

from typing import List
def maxSubArray(self, nums: List[int]) -> int:
        max_subsum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if (current_sum < 0):
                current_sum = 0
            
            current_sum += nums[i]
        
            if (current_sum > max_subsum):
                max_subsum = current_sum
        
        return max_subsum
