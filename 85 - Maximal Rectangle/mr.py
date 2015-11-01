class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        consec_col = [[0] * n for row in range(m)]
        consec_col[0] = map(int, matrix[0][:])
        for row in range(1, m):
            for col in range(n):
                if matrix[row][col] == "1":
                    consec_col[row][col] = consec_col[row - 1][col] + 1
        print(consec_col)
        return max([self.largestRectangleArea(row) for row in consec_col])

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
    matrix = ["01", "01"]
    print(Solution().maximalRectangle(matrix))
