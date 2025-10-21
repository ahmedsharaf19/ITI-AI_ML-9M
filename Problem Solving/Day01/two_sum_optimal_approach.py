    // Optimal Approach using Python
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashingMap = {}
        for idx,element in enumerate(nums):
            if (target - element) in hashingMap.keys():
                return idx, hashingMap[target - element]
            hashingMap[element] = idx