# Problem Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Submission Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1813223760/

from typing import List
class Solution:
    def findMin(nums: List[int]) -> int:
        idx = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (right + left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else :
                right = middle
            
        return nums[left]