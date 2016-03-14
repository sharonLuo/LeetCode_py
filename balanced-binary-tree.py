"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#### simple and clever
class Solution:
  # @param root, a tree node
  # @return a boolean
  def isBalanced(self, root):
    return self.getBalanceHeight(root) != -1
 
  # @param root, a tree node
  # @return a int, if the root is balanced return height, or return -1
  def getBalanceHeight(self, root):
    if root is None:
      return 0;
    leftHeight = self.getBalanceHeight(root.left)
    rightHeight = self.getBalanceHeight(root.right)
    # if left (or right) child tree is not balanced, return -1 directly to stop recursion
    if leftHeight < 0 or rightHeight < 0 or math.fabs(leftHeight - rightHeight) >1:
      return -1
    return max(leftHeight, rightHeight) + 1


################     
class Solution(object):
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if abs(self.depth(root.left)-self.depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def depth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return 1 + self.depth(root.right)
        if root.right == None:
            return 1 + self.depth(root.left)
        return 1 + max(self.depth(root.left), self.depth(root.right))
    
