# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        ptr_right = head
        count = 0
        
        if head is None:
            return None
        
        ptr = head
        length = 0
        while ptr is not None:
            ptr = ptr.next
            length += 1

        k = k % length 
        
        if k == 0: # While k is divided by the length of the linnked list, no rotation at all
            return head

        for count in range(k):
            ptr_right = ptr_right.next
            if ptr_right == None: # Hit the end, now get back to the head
                ptr_right = head

        ptr_left = head
        
        while ptr_right.next is not None: # Probe the end of the linked list with ptr_right
            ptr_right = ptr_right.next
            ptr_left = ptr_left.next

        # Do the rotation
        ptr_right.next = head
        head_new = ptr_left.next
        ptr_left.next = None

        return head_new
