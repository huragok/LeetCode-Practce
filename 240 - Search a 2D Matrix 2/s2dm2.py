class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
            
        # Initialization
        left = 0
        top = 0
        right  = n
        bottom = m
        
        return self._searchMatrix(matrix, target, left, top, right, bottom)
        
    def _searchMatrix(self, matrix, target, left, top, right, bottom):
        if target > matrix[bottom - 1][right - 1] or target < matrix[top][left]:
            return False
        if right == left + 1 and bottom == top + 1: # Only one number to check
            return matrix[top][left] == target
        elif right == left + 1: # Only one column to check
            mid_row = (top + bottom) / 2
            if target < matrix[mid_row][left]:
                return self._searchMatrix(matrix, target, left, top, right, mid_row)
            else:
                return self._searchMatrix(matrix, target, left, mid_row, right, bottom)
        elif bottom == top + 1: # Only one row to check
            mid_col = (left + right) / 2
            if target < matrix[top][mid_col]:
                return self._searchMatrix(matrix, target, left, top, mid_col, bottom)
            else:
                return self._searchMatrix(matrix, target, mid_col, top, right, bottom)
                
        else:
            mid_row = (top + bottom) / 2
            mid_col = (left + right) / 2
            if target == matrix[mid_row][mid_col]:
                return True
            if target < matrix[mid_row][mid_col]:
                return self._searchMatrix(matrix, target, mid_col, top, right, mid_row) or \
                       self._searchMatrix(matrix, target, left, mid_row, mid_col, bottom) or \
                       self._searchMatrix(matrix, target, left, top, mid_col, mid_row)
            else:
                return self._searchMatrix(matrix, target, mid_col, top, right, mid_row) or \
                       self._searchMatrix(matrix, target, left, mid_row, mid_col, bottom) or \
                       self._searchMatrix(matrix, target, mid_col, mid_row, right, bottom)
                       
if __name__ == "__main__":
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
    #matrix = [
    #          [1,   4],
    #          [2,   5]
    #        ]
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 15
    print(Solution().searchMatrix(matrix, target))
