# Problem Link: https://leetcode.com/problems/two-sum/
# Submission Link: https://leetcode.com/problems/two-sum/submissions/1807307456/

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        hashingMap = {}
        for idx,element in enumerate(nums):
            if (target - element) in hashingMap.keys():
                return idx, hashingMap[target - element]
            hashingMap[element] = idx