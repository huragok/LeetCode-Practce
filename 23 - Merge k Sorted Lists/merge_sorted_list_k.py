#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):

        lists_next = [node for node in lists if node is not None]
        if len(lists_next) == 0:
            return None

        anchor = ListNode(None)
        ptr = anchor
        heapify(lists_next)
        while len(lists_next) > 0:
            node = extract_min(lists_next)
            ptr.next = node
            ptr = ptr.next
            if node.next is not None:
                sift_up(lists_next, node.next)

        return anchor.next

# Build a heap given a list of nodes
def heapify(lists):
    n = len(lists)
    for idx in range((n - 1) // 2, -1, -1):
        sift_down(lists, idx)

    return

# Assume lists[bound_left + 1 : bound_right] has already been a heap, make lists[bound_left : bound_right] a heap
def sift_down(lists, idx):
    idx_l = 2 * idx + 1
    idx_r = idx_l + 1

    bound_right = len(lists)
    while idx_l < bound_right: # can still sift down
        if idx_l < bound_right and lists[idx_l].val < lists[idx].val:
            idx_min = idx_l
        else:
            idx_min = idx

        if idx_r < bound_right and lists[idx_r].val < lists[idx_min].val:
            idx_min = idx_r

        if idx_min != idx:
            (lists[idx_min], lists[idx]) = (lists[idx], lists[idx_min])
            idx = idx_min
            idx_l = 2 * idx + 1
            idx_r = idx_l + 1
        else:
            return

    return

# lists is already a heap, append node to this heap via a sift up procedure
def sift_up(lists, node):
    lists.append(node)
    idx = len(lists) - 1
    idx_parent = (idx - 1) // 2
    while idx_parent >= 0 and lists[idx_parent].val > lists[idx].val:
        (lists[idx_parent], lists[idx]) = (lists[idx], lists[idx_parent])
        idx = idx_parent
        idx_parent = (idx - 1) // 2

    return

# Extract the min node from lists and maintain the maintain the heap property
def extract_min(lists):
    if len(lists) == 1:
        return lists.pop(0)
    else:
        (lists[0], lists[-1]) = (lists[-1], lists[0])
        node = lists.pop()
        sift_down(lists, 0)
        return node

def linklist_to_list(head):
    ptr = ListNode(None)
    ptr.next = head
    l = []
    while ptr.next is not None:
        ptr = ptr.next
        l.append(ptr.val)

    return l

def listlists_to_linklistlists(listlists):
    lists = []
    for l in listlists:
        anchor = ListNode(None)
        ptr = anchor
        for n in l:
            ptr.next = ListNode(n)
            ptr = ptr.next
        lists.append(anchor.next)

    return lists

if __name__ == "__main__":

    input = [[2, 4, 6],[2, 4, 6, 8], [1,5,7]]
    lists =  listlists_to_linklistlists(input)
    head = lists[0]
    # heapify(lists)
    # v = [node.val for node in lists]
    # print(v)
    # sift_up(lists, ListNode(5))
    # v = [node.val for node in lists]
    # print(v)
    # m = extract_min(lists)
    # v = [node.val for node in lists]
    # print(v)
    # print(m.val)
    head = Solution().mergeKLists(lists)
    print(linklist_to_list(head))