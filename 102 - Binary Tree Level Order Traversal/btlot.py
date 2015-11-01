# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if root is None:
            return []
            
        q = [root]
        output = []
        count_level = 1
        
        while q:
            level = []
            count = 0
            for i in range(count_level):
                node = q.pop(0)
                level.append(node.val)
                
                if node.left is not None:
                    q.append(node.left)
                    count += 1
                if node.right is not None:
                    q.append(node.right)
                    count += 1
                    
            count_level = count
            output.append(level)
        
        return output
