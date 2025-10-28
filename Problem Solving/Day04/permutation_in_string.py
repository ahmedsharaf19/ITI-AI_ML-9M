# Problem Link : https://leetcode.com/problems/permutation-in-string/description/
# Submission Link : https://leetcode.com/problems/permutation-in-string/submissions/1812052625/

def checkInclusion(s1: str, s2: str) -> bool:
    windwo_size = len(s1)
    if len(s1) > len(s2): 
        return False
    s1 = sorted(s1)
    for i in range(len(s2)):
        sub = s2[i: i + windwo_size]
        if s1 == sorted(sub):
            return True
    return False
