# Problem Link : https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Submission Link : https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1813195701/

from typing import List
def search(nums: List[int], target: int) -> int:
        idx = -1
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (right + left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else :
                right = middle

        idx = left
        if target >= nums[0]:
            left = 0
            right = idx - 1
        else:
            left = idx 
            right = len(nums) - 1

        idx = -1
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