# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root:
            return []
            
        q = [root]
        output = []
        while q:
            q_new = []
            level = []
            for node in q:
                level.append(node.val)
                if node.left:
                    q_new.append(node.left)
                if node.right:
                    q_new.append(node.right)
                    
            q = q_new
            output.insert(0, level)
        return output            
