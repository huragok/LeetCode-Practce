#!/usr/bin/env python3

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_ind = {n: i for i, n in enumerate(num)}
        print(num_ind)
        for i_first in range(len(num) - 1):
            n_first = num[i_first]
            n_second = target - n_first
            try:
                i_second = num_ind[n_second]
            except KeyError:
                continue
            else:
                if i_second > i_first:
                    break

        return (i_first + 1, i_second + 1)

if __name__ == "__main__":
    num = (3, 2, 4)
    target = 6
    index1, index2 = Solution().twoSum(num, target)
    print("Input: number={0}, target={1}".format(num, target))
    print("Output: index1={0}, index2={1}".format(index1, index2))
