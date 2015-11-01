# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        first = None # The first swapped node
        second = None # The second swapped node
        pre = None # The previous node checked
        while root is not None:
            if root.left is not None:
                # Find the inorder pre node
                temp = root.left
                while temp.right is not None and temp.right != root:
                    temp = temp.right
                    
                if temp.right is not None: # temp == root, remove the thread
                    # check swap
                    if pre is not None and pre.val >= root.val:
                        if first is None:
                            first = pre
                            second = root
                        else:
                            second = root
                    pre = root
                    
                    temp.right = None
                    root = root.right
                else: # temp == None, add the thread
                    temp.right = root
                    root = root.left                    
            else:
                # check swap
                if pre is not None and pre.val >= root.val:
                    if first is None:
                        first = pre
                        second = root
                    else:
                        second = root
                pre = root
                root = root.right
        
        (first.val, second.val) = (second.val, first.val)
        return
        
        
