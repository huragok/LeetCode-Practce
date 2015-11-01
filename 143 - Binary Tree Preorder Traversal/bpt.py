# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        #Let's do this with Morris Traversel
        output = []
        while root:
            if root.left is None:
                output.append(root.val)
                root = root.right
            else:
                # find the prenode 
                temp = root.left
                while temp.right is not None and temp.right != root:
                    temp = temp.right
                    
                if temp.right is None:
                    output.append(root.val)
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None
                    root = root.right
                    
        return output
