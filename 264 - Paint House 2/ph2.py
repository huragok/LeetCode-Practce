class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        
        # Initialization
        mc = costs[0]
        print(mc)
        # Start the iteration
        for house in xrange(1, n):
            idx_0, idx_1 = self.findMinTwo(mc)
            min_cost, min_second_cost = mc[idx_0], mc[idx_1]
            print(idx_0, idx_1)
            for color in xrange(k):
                if color != idx_0:
                    mc[color] = min_cost + costs[house][color]
                else:
                    mc[color] = min_second_cost + costs[house][color]
                    
            print(mc)
        return min(mc)
                
            
    def findMinTwo(self, cost):
        # Find the index of the first and second smallest cost
        idx_0 = None
        idx_1 = None
        min_cost = None
        min_second_cost = None
        for idx, c in enumerate(cost):
            if min_cost is None or c < min_cost:
                idx_1 = idx_0
                idx_0 = idx
                min_second_cost = min_cost
                min_cost = c
            elif min_second_cost is None or c < min_second_cost:
                idx_1 = idx
                min_second_cost = c
                
        return (idx_0, idx_1)
        
if __name__ == "__main__":
    costs = [[20,9,9,8,1,9,14,8,16,20,4,15,13,15,5],[10,4,4,11,16,19,3,13,2,14,8,18,19,4,15],[6,6,19,11,6,7,4,3,2,13,8,7,13,12,10],[13,3,2,10,19,6,9,9,16,19,5,2,17,18,20],[5,2,20,1,14,5,12,13,11,10,12,7,17,15,10],[19,9,19,3,13,11,5,5,11,7,18,15,20,15,19]]
    print(Solution().minCostII(costs))

