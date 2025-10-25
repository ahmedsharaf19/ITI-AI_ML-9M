# Problem Link : https://leetcode.com/problems/container-with-most-water/description/
# Submission Link : https://leetcode.com/problems/container-with-most-water/submissions/1809395693/

from typing import List
def maxArea(height: List[int]) -> int:
    maxContainerSize = 0
    currentContainerSize = 0
    startPointer = 0
    endPointer = len(height) - 1
    while startPointer <  endPointer:
        x_diff = endPointer - startPointer
        if height[startPointer] <= height[endPointer]:
            currentContainerSize = x_diff * height[startPointer]
            startPointer += 1
        else :
            currentContainerSize = x_diff * height[endPointer]
            endPointer -= 1
        
        if (maxContainerSize < currentContainerSize):
            maxContainerSize =  currentContainerSize
            
    return maxContainerSize