# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
            
        ptr_removed = head
        ptr_probe = head.next
        val_current = head.val
        
        while ptr_probe is not None:
            if ptr_probe.val != val_current:
                val_current = ptr_probe.val
                ptr_removed.next = ptr_probe
                ptr_removed = ptr_probe
            ptr_probe = ptr_probe.next
            
        ptr_removed.next = None
        return head
