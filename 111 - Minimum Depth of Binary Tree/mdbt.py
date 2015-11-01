# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
            
        q = [root]
        depth = 1
        while q:
            q_new = []
            for node in q:
                if node.left is None and node.right is None: # Find a leaf node
                    return depth
                if node.left is not None:
                    q_new.append(node.left)
                if node.right is not None:
                    q_new.append(node.right)
                    
            q = q_new
            depth += 1
        return
