# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        anchor = ListNode(None)
        anchor.next = head
        ptr_sorted = head
        ptr_next = head.next
        while ptr_next:
            node_next = ptr_next
            ptr_next = ptr_next.next
            
            if node_next.val >= ptr_sorted.val: #this node is concatenated to the end of the sorted part
                ptr_sorted.next = node_next
                ptr_sorted = node_next
            else:
                ptr_prev = anchor
                while ptr_prev != ptr_sorted:
                    if node_next.val <= ptr_prev.next.val:
                        node_next.next = ptr_prev.next
                        ptr_prev.next = node_next
                        break
                    ptr_prev = ptr_prev.next
                
        ptr_sorted.next = None # The end of the linked list
        return anchor.next
        
    # print linked list
    def _print(self, head):
        s = ''
        ptr = head
        while ptr is not None:
            s += "{0}".format(ptr.val)
            s += ' -> '
            ptr = ptr.next
        s += 'None'
        print(s)
            
if __name__ == "__main__":
    nums = [0, 1, 2, 3]
    anchor = ListNode(None)
    ptr = anchor
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
        
    head = Solution().insertionSortList(anchor.next)
    Solution()._print(head)
                
            
