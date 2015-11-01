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
        if root is None:
            return None
        elif root == p:
            return p
        elif root == q:
            return q
            
        ancestor_left = self.lowestCommonAncestor(root.left, p, q)
        ancestor_right = self.lowestCommonAncestor(root.right, p, q)
        
        if ancestor_left is None and ancestor_right is None:
            return None
        elif ancestor_left is None:
            return ancestor_right
        elif ancestor_right is None:
            return ancestor_left
        else:
            return root
