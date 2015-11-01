# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        output = [None]
        self._maxPathSum(root, output)
        return output[0]
    
    # Return the maximum path sum whose one end is at root
    def _maxPathSum(self, root, output):
        if root is None:
            return 0 
            
        left = max([self._maxPathSum(root.left, output), 0])
        right = max([self._maxPathSum(root.right, output), 0])
        
        path_sum = left + root.val + right
        if output[0] is None or path_sum > output[0]:
            output[0] = path_sum
            
        return max([left, right]) + root.val
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root))
