# Problem Link : https://leetcode.com/problems/add-two-numbers/description/
# Submission Link : https://leetcode.com/problems/add-two-numbers/submissions/1813927350/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        head = ListNode()
        dummy = head

        while l1 or  l2:
            currentNode = None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum += val1 + val2
            if sum // 10 == 0:
                currentNode = ListNode(sum)
                sum = 0
            else :
                currentNode = ListNode(sum % 10)
                sum //= 10
            dummy.next = currentNode
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None   
            
        if sum != 0:
            dummy.next = ListNode(sum)
        return head.next
        
            
