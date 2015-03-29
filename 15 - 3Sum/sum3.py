#!/usr/bin/env python

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        l_num = len(num)
        if l_num < 3:
            return []
            
        num_sorted = sorted(num)
        list_3sum = []
        for left in range(l_num - 2):
            if num_sorted[left] > 0:
                break
            mid = left + 1
            right = l_num - 1
            
            while right > mid:
                sum_mr = num_sorted[mid] + num_sorted[right]
                if sum_mr == -num_sorted[left]:
                    list_3sum.append((num_sorted[left], num_sorted[mid], num_sorted[right]))
                    mid += 1
                elif sum_mr < -num_sorted[left]:
                    mid += 1
                else:
                    right -= 1
                    
        list_returned = [list(tuple_3sum) for tuple_3sum in set(list_3sum)]
        return list(set(list_3sum)
        
if __name__ == "__main__":
    num = [-1,0,1,2,-1,-4]
    sol = Solution()
    for three_tuple in sol.threeSum(num):
        print(three_tuple)
