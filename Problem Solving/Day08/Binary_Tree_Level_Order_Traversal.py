# Problem Link : https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Sunmission Link : https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1841732683/


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left

         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = list()
        ans = list()
        queue.append(root)
        while len(queue) != 0:
            level = []
            sz = len(queue)
            while sz:
                node = queue.pop(0)
                level.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sz -= 1
            ans.append(level)
        
        return ans
        