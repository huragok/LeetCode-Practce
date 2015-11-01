# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
            
        s = [root]
        count_level = 1
        output = []
        toggle = True
        while s:
            count = 0
            level = []
            level_next = []
            for i in range(count_level):
                node = s.pop()
                level.append(node.val)
                if toggle:
                    if node.left is not None:
                        level_next.append(node.left)
                        count += 1
                    if node.right is not None:
                        level_next.append(node.right)
                        count += 1
                else: 
                    if node.right is not None:
                        level_next.append(node.right)
                        count += 1
                    if node.left is not None:
                        level_next.append(node.left)
                        count += 1
                        
            output.append(level)
            s = level_next
            toggle = not toggle
