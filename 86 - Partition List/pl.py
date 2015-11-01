# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        anchor = ListNode(None)
        ptr_last_less = anchor
        ptr_first_greater = None
        ptr_last_greater = ListNode(None)
        ptr_probe = head
        while ptr_probe is not None:
            ptr_next = ptr_probe.next
            if ptr_probe.val < x:
                ptr_last_less.next = ptr_probe
                ptr_last_less = ptr_last_less.next
                ptr_last_less.next = ptr_first_greater
            else:
                ptr_last_greater.next = ptr_probe
                ptr_last_greater = ptr_last_less.next
                ptr_last_greater.next = ptr_first_greater
                if ptr_first_greater is None:
                    ptr_first_greater = ptr_last_greater
                    ptr_last_less.next = ptr_first_greater
            ptr_probe = ptr_next
        
        ptr_last_greater.next = None    
        return anchor.next
