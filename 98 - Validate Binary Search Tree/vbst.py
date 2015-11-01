# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        return self._isValidBST(self, root, 'l', 'u'):
            
    def _isValidBST(self, root, lb, ub):
        if root is None:
            return True
        elif ub != 'u' and root.val >= ub:
            return False
        elif lb != 'l' and root.val <= lb:
            return False
        elif not self._isValidBST(root.left, lb, root.val):
            return False
        elif not self._isValidBST(root.right, root.val, ub):
            return False
        else:
            return True
        
