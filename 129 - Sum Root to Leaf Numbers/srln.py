# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if root is None:
            return 0
        else:
            total_sum = [0]
            self._sumNumbers(root, root.val, total_sum)
            return total_sum[0]
    
    def _sumNumbers(self, root, partial_sum, total_sum):
        if root is None:
            return
        elif root.left is None and root.right is None: # A leaf node
            total_sum += partial_sum
        else:
            if root.left is not None:   
                partial_sum_new = partial_sum * 10 + root.left.val
                self._sumNumbers(root.left, partial_sum_new, total_sum)
            if root.right is not None:
                partial_sum_new = partial_sum * 10 + root.right.val
                self._sumNumbers(root.right, partial_sum_new, total_sum)
            
        return
