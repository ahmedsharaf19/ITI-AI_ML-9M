# Problem Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Submission Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1809534449


from typing import List
def removeDuplicates(self, nums: List[int]) -> int:

    uniqueElement =sorted(set(nums))[::-1]

    k = len(uniqueElement)

    for i in range(0, k):

        nums[i] = uniqueElement.pop()

    return k
