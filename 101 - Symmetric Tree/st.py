# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True # If is a leef node or empty node, return true
        
        return self._isSymmetric(root.left, root.right)
        
        
    def _isSymmetric(self, root_l, root_r):
        if root_l is None and root_r is None:
            return True
        elif root_l is None or root_r is None:
            return False
        elif root_l.val != root_r.val:
            return False
        else:
            return self._isSymmetric(root_l.left, root_r.right) and self._isSymmetric(root_l.right, root_r.left)
                
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    
    print(Solution().isSymmetric(root))
