# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        elif head.next is None:
            return False
            
        ptr_1x = head
        ptr_2x = head.next
        while ptr_1x is not None and ptr_2x is not None:
            if ptr_1x == ptr_2x:
                return True
            ptr_1x = ptr_1x.next
            ptr_2x = ptr_2x.next
            if ptr_2x is not None:
                ptr_2x = ptr_2x.next
            else:
                return False
        return False
                
            
