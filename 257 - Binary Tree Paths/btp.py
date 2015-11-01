# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [str(root.val)]
        else:
            self.result = []
            path_partial = str(root.val)
            if root.left is not None:
                self.dps(root.left, path_partial)
            if root.right is not None:
                self.dps(root.right, path_partial)
            return self.result
        
    def dps(self, root, path_partial):
        path_partial +=  '->' + str(root.val)
        if root.left is None and root.right is None:
            self.result.append(path_partial)
        else:
            if root.left is not None:
                self.dps(root.left, path_partial)
            if root.right is not None:
                self.dps(root.right, path_partial)
        return
