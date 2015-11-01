# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        reverse = None
        ptr = head
        while ptr is not None:
            tmp = ptr
            ptr = ptr.next
            tmp.next = reverse
            reverse = tmp
            
        return reverse
