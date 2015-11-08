package rll2;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == n) return head;
		ListNode anchor = new ListNode(0);
        anchor.next = head;
        
        ListNode ptrTailBefore, ptrHeadAfter;
        ListNode ptr = anchor;
        for (int i = 0; i < m - 1; i++) {
        	ptr = ptr.next;
        }
        ptrTailBefore = ptr;
        for (int i = m - 1; i < n; i++) {
        	ptr = ptr.next;
        }
        ptrHeadAfter = ptr.next;
        
        ptr = ptrTailBefore.next;
        ListNode ptrTailReversed = ptr;
        ptrTailBefore.next = null;
        for (int i = m; i <= n;  i++) {
        	ListNode ptrTmp = ptrTailBefore.next;
        	ListNode ptrNew = ptr.next;
        	ptrTailBefore.next = ptr;
        	ptr.next = ptrTmp;
        	ptr = ptrNew;
        }
        ptrTailReversed.next = ptrHeadAfter;
        return anchor.next;
    }
	
}
