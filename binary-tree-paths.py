"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


def binaryTreePaths(self, root):
    if not root:
        return []
    if not root.left and not root.right:
        return [str(root.val)]
    treepaths = [str(root.val)+'->'+path for path in self.binaryTreePaths(root.left)]
    treepaths += [str(root.val)+'->'+path for path in self.binaryTreePaths(root.right)]
    return treepaths



 ###########

 class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        buf = self.helper(root)
        result = []
        for i in range(len(buf)):
            result.append("->".join(buf[i]))
        return result
        
    def helper(self, root):
        if not root:
            return []
        result = []
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not left and not right:
            return [[str(root.val)]]
        for p in left:
            result.append([str(root.val)]+p)
        for p in right:
            result.append([str(root.val)]+p)
        return result
            
        
        
        
