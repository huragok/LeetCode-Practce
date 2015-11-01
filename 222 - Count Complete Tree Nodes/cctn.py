# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        node = root
        count = 0
        while node is not None:
            depth_left = self.getDepthLeft(node.left)
            depth_right = self.getDepthLeft(node.right)
            if depth_left == depth_right: # Left node is still a complete tree, right node is not
                count += 2 ** (depth_left + 1)
                node = node.right
            else: # Left node is not a complete tree, right node is
                count += 2 ** (depth_right + 1)
                node = node.left
        return count
        
    # Get the depth of the leftmost path from root
    def getDepthLeft(self, root):
            
        node = root
        depth = -1
        while node is not None:
            node = node.left
            depth += 1
        return depth
