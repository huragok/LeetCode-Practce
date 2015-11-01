# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.k = k
        self.result = []
        self.target = target
        self.inOrder(root)
        
    def inOrder(self, root):
        if root is None:
            return
        else:
            self.inOrder(root.left)
            
            if len(self.result) < self.k:
                self.result.append(root.val)
            elif abs(root.val - self.target) < abs(self.result[0] - self.target):
                self.result.append(root.val)
                self.result.pop[0]
            else:
                return
            
            self.inOrder(root.right)
            return
        
