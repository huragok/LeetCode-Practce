class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        # Binary search for the row
        l = 0
        r = m - 1
        
        if target < matrix[l][0]:
            return False
        elif target >= matrix[r][0]:
            row = r
        else:
            while r - l > 1:
                i = (r + l) / 2
                if matrix[i][0] <= target:
                    l = i
                else:
                    r = i
                    
            row = l
        print(row)
         
        # Binary search for the col
        l = 0
        r = n - 1
        print(r)
        if target > matrix[row][r]:
            return False
        elif target == matrix[row][r]:
            return True
        else:
            while r - l > 1:
                i = (r + l) / 2
                if matrix[row][i] <= target:
                    l = i
                else:
                    r = i
                    
            col = l
            print(col)
            return (matrix[row][col] == target)
            
if __name__ == "__main__":
    matrix = [[1,   3,  5,  7], [10, 11, 16, 20],  [23, 30, 34, 50]]
    target = 4
    matrix = [[1], [3]]
    target = 1
    print(Solution().searchMatrix(matrix, target))
