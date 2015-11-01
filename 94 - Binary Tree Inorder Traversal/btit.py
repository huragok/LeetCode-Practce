# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        stack = []
        output = []
        
        stack.append(root)
        
        while stack:
            if stack[-1].left is not None:
                stack.append(stack[-1].left)
            else:
                node_right = stack[-1].right
                output.append(stack.pop())
                if node_right is not None:
                    stack.append(node_right)
                    
        return output
            
