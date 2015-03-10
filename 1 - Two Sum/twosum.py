#!/usr/bin/env python3

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for i_first in range(len(num) - 1):
            n_first = num[i_first]
            n_second = target - n_first
            try:
                i_second = num.index(n_second, i_first + 1)
            except ValueError:
                continue
            else:
                break

        return (i_first + 1, i_second + 1)

if __name__ == "__main__":
    num = (2, 7, 11, 15)
    target = 9
    index1, index2 = Solution().twoSum(num, target)
    print("Input: number={0}, target={1}".format(num, target))
    print("Output: index1={0}, index2={1}".format(index1, index2))
