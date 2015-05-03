#!/usr/bin/env python

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        l_num = len(num)
        if l_num < 3:
            return []
        
        num_sorted = sorted(num)

        dist_min = float('inf')
        sign = 1
        for left in range(l_num - 2):
            mid = left + 1
            right = l_num - 1
            
            while right > mid:
                dist = num_sorted[left] + num_sorted[mid] + num_sorted[right] - target
                if -dist_min < dist < dist_min:
                    (dist_min, sign) = (dist, 1) if dist > 0 else (-dist, -1)
                if dist == 0:
                    return target
                elif dist > 0:
                    right -= 1
                else:
                    mid += 1
                    
        return target + sign * dist_min

if __name__ == "__main__":
    num = [0, 1, 2]
    target = 3
    sol = Solution()
    print(sol.threeSumClosest(num, target))
