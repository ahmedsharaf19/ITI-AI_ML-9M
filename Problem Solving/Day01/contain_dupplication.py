# Problem Link: https://leetcode.com/problems/contains-duplicate/
# Submission Link: https://leetcode.com/problems/contains-duplicate/submissions/1809372890/

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
        numbersSeened = set()
        for number in nums:
            if number in numbersSeened:
                return True
            numbersSeened.add(number)
        return False
