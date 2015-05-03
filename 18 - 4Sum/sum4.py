#!/usr/bin/env python

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        l_num = len(num)
        hash_sum_to_2idx = {}
        set_4sum = set()
        for i in range(l_num - 1):
            for j in range(i+1, l_num):
                hash_sum_to_2idx.setdefault(num[i]+num[j], []).append((i, j))
        #print(hash_sum_to_2idx)        

        for sum_12 in hash_sum_to_2idx.keys():
            if sum_12 > target / 2:
                continue
            sum_34 = target - sum_12
            list_idx_12 = hash_sum_to_2idx.get(sum_12)
            list_idx_34 = hash_sum_to_2idx.get(sum_34, [])
            for idx_1, idx_2 in list_idx_12:
                for idx_3, idx_4 in list_idx_34:
                    if idx_1 != idx_3 and idx_1 != idx_4 and idx_2 != idx_3 and idx_2 != idx_4:
                        set_4sum.add(tuple(sorted((num[idx_1], num[idx_2], num[idx_3], num[idx_4]))))

        list_4sum = [list(tuple_4sum) for tuple_4sum in set_4sum]
        return list_4sum
                        
if __name__ == "__main__":
    num = [1,0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    for four_tuple in sol.fourSum(num, target):
        print(four_tuple)
