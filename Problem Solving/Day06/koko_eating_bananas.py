# Problem Link : https://leetcode.com/problems/koko-eating-bananas/description/
# Submission Link : https://leetcode.com/problems/koko-eating-bananas/submissions/1813871716/

from typing import List
from math import ceil
def minEatingSpeed(piles: List[int], h: int) -> int:
    left = 1
    right = max(piles)
    k = -1
    while left <= right:
        hours = 0
        middle = (right + left) // 2
        for pile in piles:
            hours += ceil(pile / middle)
        
        if hours <= h:
            k = middle
            right = middle - 1
        else :
            left = middle + 1
        
    return k