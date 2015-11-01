# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if p.val > q.val:
            p, q = q, p
            
        ptr = root
        while True:
            if ptr.val < p.val:
                ptr = ptr.right
            elif ptr.val > q.val:
                ptr = ptr.left
            else:
                return ptr
