# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}       
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None: # a leaf node
            return True if root.val == sum else False
            
        return self._hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

                
