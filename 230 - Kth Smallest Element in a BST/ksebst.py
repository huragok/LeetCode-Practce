# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        self.kmin = None
        self.countNode(root, k)
        return self.kmin
        
    def countNode(self, root, k):
        if root is None:
            return 0
            
        count_left = self.countNode(root.left, k)
        if count_left == k - 1:
            self.kmin = root.val
        count_right = self.countNode(root.right, k - count_left - 1)
        return count_left + count_right + 1
