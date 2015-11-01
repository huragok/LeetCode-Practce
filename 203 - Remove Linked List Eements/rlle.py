# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        anchor = ListNode(None)
        ptr_prev = anchor
        ptr_prev.next = head
        ptr = head
        while ptr:
            if ptr.val == val:
                ptr_prev.next = ptr.next
            else:
                ptr_prev = ptr
            ptr = ptr.next
            
        return anchor.next
                
        
