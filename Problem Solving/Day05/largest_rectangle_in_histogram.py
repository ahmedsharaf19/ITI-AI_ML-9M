# Problem Link : https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# Submission Link : https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/1814019909/

from typing import List
def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    area = 0
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = 0
            if stack :
                width = i - stack[-1] - 1
            else :
                width = i
            area = max(area, height * width)
        stack.append(i)
    while stack:
        height = heights[stack.pop()]
        if stack:
            width = len(heights) - stack[-1] - 1
        else :
            width = len(heights)
        area = max(area, height * width)
    
    return area