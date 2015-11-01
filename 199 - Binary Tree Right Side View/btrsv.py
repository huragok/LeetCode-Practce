# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rsv = []
        level = [root]
        while len(level) > 0:
            level_new = []
            for node in level:
                if node.left is not None:
                    level_new.append(node.left)
                if node.right is not None:
                    level_new.append(node.right)
            rsv.append(level[-1].val)
            level = level_new
            
        return rsv
