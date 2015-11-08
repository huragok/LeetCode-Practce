package msa;

public class Solution {
	public void merge(int[] nums1, int m, int[] nums2, int n) {
		int ptr1 = m - 1;
		int ptr2 = n - 1;
		int ptrMerged = m + n - 1;
		while (ptr2 >= 0) {
			if (ptr1 < 0 || nums1[ptr1] <= nums2[ptr2]) {
				nums1[ptrMerged] = nums2[ptr2];
				ptr2--;
			} else {
				nums1[ptrMerged] = nums1[ptr1];
				ptr1--;
			}
			ptrMerged--;
		}
    }
}
