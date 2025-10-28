# Problem Link : https://leetcode.com/problems/linked-list-cycle/description/
# Submission Link : https://leetcode.com/problems/linked-list-cycle/submissions/1813910351/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map = {}
        while head:
            if head.next not in map:
                map[head] = head.next
                head = head.next
                continue 
            return True
        return False
            