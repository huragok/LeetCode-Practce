# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
            
        root.next = None
        q = [root]
        while q:
            q_new = []
            for node in q:
                if node.left:
                    q_new.append(node.left)
                if node.right:
                    q_new.append(node.right)
            n = len(q_new)
            if n > 0:
                for idx in range(0, n - 1):
                    q_new[idx].next = q_new[idx + 1]                
                q_new[n-1].next = None
            
            q = q_new
            
        return
