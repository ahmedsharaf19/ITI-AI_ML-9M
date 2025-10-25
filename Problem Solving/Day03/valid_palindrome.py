# Problem Link : https://leetcode.com/problems/valid-palindrome/description/
# Submission Link : https://leetcode.com/problems/valid-palindrome/submissions/1809196650/

from typing import List
import re

def isPalindrome(s: str) -> bool:
    s = s.lower()  
    s = re.sub("[^a-zA-Z0-9]", "", s)
    if (len(s) == 0):
        return True
    
    pointer_first = 0
    pointer_end = len(s) - 1
    while(pointer_first < pointer_end):
        while(not s[pointer_first].isalnum()):
            pointer_first += 1
        
        while(not s[pointer_end].isalnum()):
            pointer_end -= 1
        
        if (s[pointer_first] != s[pointer_end]):
            return False
        
        pointer_first += 1
        pointer_end -= 1
    
    return True

    
