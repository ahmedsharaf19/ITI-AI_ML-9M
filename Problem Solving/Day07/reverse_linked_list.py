# Problem Link : https://leetcode.com/problems/reverse-linked-list/description/
# Sunmission Link : https://leetcode.com/problems/reverse-linked-list/submissions/1813284257/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:        
    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous