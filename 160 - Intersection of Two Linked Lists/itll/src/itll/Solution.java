package itll;

public class Solution {
	
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) {
			val = x;
			next = null;
		}
	}
	
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lA = length(headA);
        int lB = length(headB);
        
        if (lA > lB) { // Make sure lA <= lB
        	ListNode nodeTmp = headA; headA = headB; headB = nodeTmp;
        	int lTmp = lA; lA = lB; lB = lTmp;
        }
        
        ListNode ptrA = headA;
        ListNode ptrB = headB;
        for (int i = 0; i < lB - lA; i++) ptrB = ptrB.next;
        
        while (ptrB != null) {
        	if (ptrA == ptrB) return ptrA;
        	ptrA = ptrA.next; ptrB = ptrB.next;
        }
        return null;
    }
	
	private int length(ListNode head) {
		int l = 0;
		ListNode ptr = head;
		while (ptr != null) {
			l++;
			ptr = ptr.next;
		}
		return l;
	}
}
