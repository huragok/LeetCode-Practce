class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        if m ==0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
            
        land = {(row, col) for row in range(m) for col in range(n) if grid[row][col] == '1'}
        count_island = 0
        while len(land) > 0: # Perform a bps
            point = land.pop()
            border = [point]
            while len(border) > 0:
                border_new = []
                for pb in border:
                    for neighbor in [(pb[0] - 1, pb[1]), (pb[0] + 1, pb[1]), (pb[0], pb[1] - 1), (pb[0], pb[1] + 1)]:
                        if neighbor in land:
                            border_new.append(neighbor)
                            land.remove(neighbor)
                          
                border = border_new
            count_island += 1
           
        return count_island    
        
