# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        output = []
        self._pathSum(root, sum, [], output)
        return output
        
        
    def _pathSum(self, root, sum, path, output):
        if not root:
            return
        elif root.left is None and root.right is None: # Leaf node
            if root.val == sum:
                path.append(root.val)
                output.append(path)
                
        elif root.left is None or root.right is None: # No need to copy the path
            path.append(root.val)
            if root.left is not None:
                self._pathSum(root.left, sum - root.val, path, output)
            if root.right is not None:
                self._pathSum(root.right, sum - root.val, path, output)
        else: # need to copy the path once for the right child
            path.append(root.val)
            path_copy = path[:]
            self._pathSum(root.left, sum - root.val, path, output)
            self._pathSum(root.right, sum - root.val, path_copy, output)
            
        return
