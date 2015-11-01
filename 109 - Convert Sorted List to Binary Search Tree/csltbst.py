# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        l = 0 # Length of the linked list
        ptr = head
        while ptr:
            ptr = ptr.next
            l += 1
            
        return self._sortedListToBST([head], 0, l)
        
    def _sortedListToBST(self, head_writable, start, end):
        l = end - start
        if l <= 0:
            return None
        elif l == 1:
            node = TreeNode(head_writable[0].val)
            head_writable[0] = head_writable[0].next
            return node
            
        mid = start + (l - 1) / 2
        root = TreeNode(None)
        root.left = self._sortedListToBST(head_writable, start, mid)
        root.val = head_writable[0].val
        head_writable[0] = head_writable[0].next
        root.right = self._sortedListToBST(head_writable, mid + 1, end)
        return root
