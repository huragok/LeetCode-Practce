class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        stack_height = [-1]
        stack_width_left = [0]
        
        max_area = 0
        
        for h in height:
            if h >= stack_height[-1]:
                stack_height.append(h)
                stack_width_left.append(1)
            else:
                w = 0
                while stack_height[-1] > h:
                    h_top = stack_height.pop()
                    w += stack_width_left.pop()
                    if h_top * w > max_area:
                        max_area = h_top * w
                        
                stack_height.append(h)
                stack_width_left.append(w + 1)
                
        # Now pop what is left in the stacks
        w = 0
        while stack_height[-1] >= 0:
            h_top = stack_height.pop()
            w += stack_width_left.pop()
            if h_top * w > max_area:
                max_area = h_top * w
                
        return max_area
        
if __name__ == "__main__":
    height = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(height))
