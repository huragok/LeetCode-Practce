# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        anchor = ListNode(None)
        ptr = anchor

        head_cur_pair = head

        while head_cur_pair is not None and head_cur_pair.next is not None: # There is still a full pair to swap
            head_next_pair = head_cur_pair.next.next
            ptr.next = head_cur_pair.next
            ptr = ptr.next
            ptr.next = head_cur_pair
            ptr = ptr.next

            head_cur_pair = head_next_pair

        if head_cur_pair is not None: # There are odd number of nodes in the linked list, one last node left, no swap
            ptr.next = head_cur_pair
            ptr = ptr.next

        ptr.next = None

        return anchor.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    Solution().swapPairs(head)
