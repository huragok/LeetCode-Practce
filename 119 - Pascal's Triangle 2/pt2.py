class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, rowIndex):
        rowIndex += 1
        if rowIndex < 1:
            return []
        level = [1]
        
        for row in range(1, rowIndex):
            level_new = [1]
            for col in range(row - 1):
                level_new.append(level[col] + level[col + 1])
            level_new.append(1)
            level = level_new
            
        return level
        
if __name__ == "__main__":
    print(Solution().generate(3))
