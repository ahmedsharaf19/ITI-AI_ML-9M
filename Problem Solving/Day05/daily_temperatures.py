# Problem Link : https://leetcode.com/problems/daily-temperatures/description/
# Submission Link: https://leetcode.com/problems/daily-temperatures/submissions/1812998177/

from typing import List
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    monotonicStack = []
    daily = [0 for t in temperatures]
    for i in range(len(temperatures)):
        while len(monotonicStack) and temperatures[i] > temperatures[monotonicStack[-1]]:
            idx = monotonicStack.pop()
            daily[idx] = i - idx
        
        monotonicStack.append(i)
    return daily