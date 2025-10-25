# Problem Link : https://leetcode.com/problems/3sum/description/
# Submission Link : https://leetcode.com/problems/3sum/submissions/1810965216


from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    result = []

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        while left < right:
            summition = num + nums[left] + nums[right]
            if summition > 0:
                right -= 1
            elif summition < 0:
                left += 1
            else :
                result.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return result
