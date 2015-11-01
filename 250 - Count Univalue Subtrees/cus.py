# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self._countUnivalueSubtrees(root)
        return self.count
        
    def _countUnivalueSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int, the value of the univalue subtrees, if any, else None
        """
        if root is None:
            return None
        elif root.left is None and root.right is None:
            self.count += 1
            return self.val
        else:
            val_left = '@'
            val_right = '@'
            if root.left is not None:
                val_left = self._countUnivalueSubtrees(root.left)
            if root.right is not None:
                val_right = self._countUnivalueSubtrees(root.right)
                
            if val_left is not None and (val_left == '@' or val_left == root.val) and \
               val_right is not None and (val_right == '@' or val_right == root.val):
                self.count += 1
                return self.val
            elseL
                return None
