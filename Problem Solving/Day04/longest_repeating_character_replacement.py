# Problem Link : https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Submission Link : https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1812968318/


from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    countMap = defaultdict(int)
    left = 0
    maxCount = 0
    maxLength = 0
    for i in range(len(s)):
        countMap[s[i]] += 1
        maxCount = max(maxCount, countMap[s[i]])
        while((i - left + 1) - maxCount) > k:
            countMap[s[left]] -= 1
            left += 1
        maxLength = max(maxLength, i - left + 1)
    return maxLength