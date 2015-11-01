# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        output = []
        anchor = TreeNode(None)
        anchor.left = root
        root = anchor
        while root:
            if root.left is None:
                root = root.right
            else:
                temp = root.left
                while temp.right is not None and temp.right != root:
                    temp = temp.right
                    
                if temp.right is None:
                    temp.right = Node
                    root = root.left
                else:
                    temp.right = None
                    output += self._reverseRightWisePath(root.left)
                    root = root.right
                
        return output
        
    def _reverseRightWisePath(self, root):
        output = []
        while root:
            output.insert(0, root.val)
            root = root.right
            
        return output
