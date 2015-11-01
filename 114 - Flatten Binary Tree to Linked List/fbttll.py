# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        node = root
        while node:
            if node.left:
                # Find the right most node in the left tree
                temp = node.left
                while temp.right:
                    temp = temp.right
                temp.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
            
        return
            
