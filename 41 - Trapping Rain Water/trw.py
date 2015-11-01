class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        volume = 0
        l = 0 # current left wall
        r = n - 1 # current right wall
        h = 0 # current water level
        
        while l < r:
            if height[l] < height[r]:
                h = max((h, height[l]))
                volume += h - height[l]
                l += 1
            else:
                h = max((h, height[r]))
                volume += h - height[r]
                r -= 1
                
        return volume
        
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
