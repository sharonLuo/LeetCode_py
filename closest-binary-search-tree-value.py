"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        cur_min = sys.maxsize
        cur = root
        while cur:
            if abs(cur.val-target)<cur_min:
                cur_min, closest = abs(cur.val-target), cur.val
            if cur.val>target:
                cur = cur.left
            elif cur.val<target:
                cur = cur.right
            else:
                return closest
        return closest

