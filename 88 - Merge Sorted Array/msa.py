class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        ptr1 = m - 1
        ptr2 = n - 1
        ptr_sorted = m + n - 1
        while ptr2 >= 0:
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[ptr_sorted] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr_sorted] = nums2[ptr2]
                ptr2 -= 1
            ptr_sorted -= 1
        return
            
            
