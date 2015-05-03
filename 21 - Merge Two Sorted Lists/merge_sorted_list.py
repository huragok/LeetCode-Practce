# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        anchor = ListNode(None)
        node = anchor
        node1 = l1
        node2 = l2
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                node.next = node1
                node = node1
                node1 = node1.next
            else:
                node.next = node2
                node = node2
                node2 = node2.next

        if node1 is None:
            node.next = node2
        else:
            node.next = node1

        return anchor.next