# Problem Link : https://leetcode.com/problems/merge-two-sorted-lists/description/
# Submission Link : https://leetcode.com/problems/merge-two-sorted-lists/submissions/1813898707/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        dummy = r
        while list1 and list2 :
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else :
                dummy.next = list2
                list2 = list2.next
        
            dummy = dummy.next
        dummy.next = list2 if list2 else list1
        return r.next

        


# List1 -> 1 -> 2 -> 3 -> None
# List2 -> 1 -> 3 -> 4

# Dummy and R To Catch First Node in megerd list

        