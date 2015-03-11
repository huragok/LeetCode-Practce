#!/usr/bin/env python
import math
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if len(A) < len(B):
            (A, B) = (B, A)
        m = len(A)
        n = len(B)
        
        if (m + n) % 2 == 1:
            l = (m + n - 1) // 2
        else:
            l = (m + n) // 2
        #print(l)
        
        if l == 0:
            return A[0]
        elif n == 0:
            if m % 2 == 1:
                return A[(m-1) // 2] 
            else:
                return (A[m // 2 - 1] + A[m // 2]) / float(2)
        elif A[l - 1] <= B[0]:
            na = l
            nb = 0
        elif l >= n and A[l - n] >= B[n - 1]:
            nb = n
            na = l - n
        elif l < n and A[0] >= B[l - 1]:
            na = 0
            nb = l
        else:
            na_upperlimit = l - 1
            na_lowerlimit = max((1, l - n + 1))
            na = (na_upperlimit + na_lowerlimit) // 2
            nb = l - na
            #print((na, nb))
            while A[na - 1] > B[nb] or A[na] < B[nb - 1]:
                if A[na - 1] > B[nb]: # Too many numbers in A
                    na_upperlimit = na - 1
                else: # Too few numbers in A
                    na_lowerlimit = na + 1
                na = (na_upperlimit + na_lowerlimit) // 2
                nb = l - na
                
        
        if (m + n) % 2 == 1:
            if na == m:
                return B[nb]
            elif nb == n:
                return A[na]
            else:
                return min((A[na], B[nb]))
        else:                    
            if na == 0:
                left = B[nb - 1]
            elif nb == 0:
                left = A[na - 1]
            else:
                left = max((A[na - 1], B[nb - 1]))
            
            if na == m:
                right = B[nb]
            elif nb == n:
                right = A[na]
            else:
                right = min((A[na], B[nb]))
            return (left + right) / float(2)
            
if __name__ == "__main__":
    A = []
    B = [2, 3]
    print("A = {0}".format(A))
    print("B = {0}".format(B))
    print("Median = {0}".format(Solution().findMedianSortedArrays(A, B)))
