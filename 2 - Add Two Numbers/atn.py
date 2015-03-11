#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def set_next(self, node):
        self.next = node
    def __str__(self):
        str_linkedlist = str(self.val)
        current = self
        while current.next is not None:
            current = current.next
            str_linkedlist += " -> " + str(current.val)
        return str_linkedlist
        
def build_linkedlist(*l):
    head = ListNode(l[0])
    current = head
    for n in l[1::]:
        current.set_next(ListNode(n))
        current = current.next
    return head
    
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        n1 = 0
        w = 1
        while l1 is not None:
            n1 += l1.val * w
            l1 = l1.next
            w *= 10
            
        n2 = 0
        w = 1
        while l2 is not None:
            n2 += l2.val * w
            l2 = l2.next
            w *= 10
            
        str_sum = str(n1 + n2)[::-1]
        head = ListNode(str_sum[0])
        current = head
        for s in str_sum[1::]:
            current.next = ListNode(int(s))
            current = current.next
        return head
            
if __name__ == "__main__":
    l1 = build_linkedlist(1, 8)
    l2 = build_linkedlist(0)
    
    l_sum = Solution().addTwoNumbers(l1, l2)
    
    print("Input: ({0}) + ({1})".format(l1, l2))
    print("Output: {0}".format(l_sum))
