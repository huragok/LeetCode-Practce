# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self._probeDepth(root)[0]
        
        
    def _probeDepth(self, root):
        if not root:
            return (True, 0)
            
        left = self._probeDepth(root.left)
        right = self._probeDepth(root.right)
        
        return (left[0] and right[0] and (-1 <= left[1] - right[1] <= 1), max((left[1], right[1])) + 1)
        
