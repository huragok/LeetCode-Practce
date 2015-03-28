#!/usr/bin/env python

class Solution:
    # @return an integer
    def maxArea(self, height):
        n = len(height) # number of lines
        l = 0
        r = n - 1
        v_max = 0
        while l < r:
            if height[l] > height[r]: # Right wall is the bottle neck, next left wall need not to be checked!
                v_max = max((v_max, height[r] * (r - l))) # update v_max
                r -= 1
            else:
                v_max = max((v_max, height[l] * (r - l))) # update v_max
                l += 1
                
        return v_max
        
if __name__ == "__main__":
    height = [2, 5, 3, 4, 6]
    print(Solution().maxArea(height))
