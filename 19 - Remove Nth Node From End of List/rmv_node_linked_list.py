# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        node_right = head
        for delay in range(n - 1): # Since n always valid
            node_right = node_right.next

        node_to_delete = head
        if node_right.next is None: # Need to delete the original head
            return head.next

        while node_right.next is not None: # Need to delete a non head node
            node_right = node_right.next
            node_left = node_to_delete
            node_to_delete = node_to_delete.next

        node_left.next = node_to_delete.next
        return head