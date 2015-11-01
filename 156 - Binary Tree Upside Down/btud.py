# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def upsideDownBinaryTree(self, root):
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        else: # Otherwise the left node must not be empty
            root_new = self.upsideDownBinaryTree(root.left)
            root.left.right = root
            root.left.left = root.right
            root.left = None
            root.right = None
            return root_new
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root_new = Solution().upsideDownBinaryTree(root)
