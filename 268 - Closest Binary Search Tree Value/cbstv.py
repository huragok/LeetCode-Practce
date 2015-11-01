# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = None
        min_abs_diff = None
        ptr = root
        while True:
            if ptr.val == target:
                return target
            else:
                if min_abs_diff is None or min_abs_diff > abs(ptr.val - target):
                    min_abs_diff = abs(ptr.val - target)
                    closest = ptr.val
                if ptr.val > target:
                    if ptr.right is None:
                        break
                    else:
                        ptr = ptr.right
                else:
                    if ptr.left is None:
                        break
                    else:
                        ptr = ptr.left
                        
        return closest
