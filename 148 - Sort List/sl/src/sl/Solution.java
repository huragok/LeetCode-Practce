package sl;
public class Solution {
	public static class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode mid = halve(head);
        ListNode head1 = sortList(head);
        ListNode head2 = sortList(mid);
        
        return merge(head1, head2);
        
    }
	
	
	private ListNode merge(ListNode head1, ListNode head2) {

		ListNode anchor = new ListNode(0);
		
		ListNode ptr1 = head1, ptr2 = head2, ptr = anchor;
		while (ptr1 != null && ptr2 != null) {
			if (ptr1.val < ptr2.val) {
				ptr.next = ptr1;
				ptr1 = ptr1.next;
				ptr = ptr.next;
			} else {
				ptr.next = ptr2;
				ptr2 = ptr2.next;
				ptr = ptr.next;
			}
			ptr.next = null;
			//System.out.println(ptr.val);
		}
		if (ptr1 == null) {
			ptr.next = ptr2;
		} else {
			ptr.next = ptr1;
		}
		return anchor.next;
		
	}
	
	private ListNode halve(ListNode head) {
		ListNode anchor = new ListNode(0);
		anchor.next = head;
		ListNode ptrFast = anchor;
		ListNode ptrSlow = anchor;
		while (ptrFast != null) {
			ptrFast = ptrFast.next;
			if (ptrFast == null) break;
			ptrFast = ptrFast.next;
			
			ptrSlow = ptrSlow.next;
		}
		
		ListNode mid = ptrSlow.next;
		ptrSlow.next = null;
		return mid;
	}
	
	public static void main(String [] args) {
		Solution.ListNode head = new Solution.ListNode(3);
		Solution.ListNode node1 = new Solution.ListNode(2);
		Solution.ListNode node2 = new Solution.ListNode(4);
		head.next = node1; node1.next = node2;
		
		ListNode result = new Solution().sortList(head);
		System.out.println(result.val);
		System.out.println(result.next.val);
		System.out.println(result.next.next.val);
	}
}
