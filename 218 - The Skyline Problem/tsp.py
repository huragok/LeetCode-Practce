import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(buildings)
        skyline = []
        buildings_pending = [] #[0] for negative height, [1] for negative right wall; taller building is prior to lower building, when two buildings are of the same height, the one with righter right wall is prior. 
        i = 0
        while i < n or buildings_pending: # There is still new buildings to add or active building to pop
            if not buildings_pending or i < n and -buildings_pending[0][1] >= buildings[i][0]: # The top active building's right wall ends after the new building's left begins
                wall = buildings[i][0] # The left wall of the new building, which is the x coordinate of the next potential point
                while i < n and buildings[i][0] == wall: # Push all the buildings starting from the same left wall
                        heapq.heappush(buildings_pending, (-buildings[i][2], -buildings[i][1]))
                        i += 1
                    
            else: # The top active building's right wall ends before the new building's left begins, now pop all active buildings that is shorter than and to the left of the top active building
                wall = -buildings_pending[0][1] # The right wall of the tallest active building, which is the x coordinate of the next potential point
                while buildings_pending and -buildings_pending[0][1] <= wall: # Pop all the buildings shadowed by the current tallest, rightmost building, including itself
                    heapq.heappop(buildings_pending)
                    
            # A new skyline is to be added
            height = 0 if not buildings_pending else -buildings_pending[0][0] # The height of a potential skyline
            if not skyline or height != skyline[-1][1]: # The first building (must be case 1), or the new potential point is not on the same height as the last one so it is a valid point
                skyline.append([wall, height])
        
        return skyline
        
if __name__ == "__main__":
    buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
    print(Solution().getSkyline(buildings))
                
