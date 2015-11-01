class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
            
        # Initialization    
        mc = costs[-1][:]
        mc_last = [None] * 3
        for idx in xrange(n - 2, -1, -1):
            mc_last = mc[:]
            for color in range(3):
                mc[color] = costs[idx][color] + min([mc_last[p] for p in range(3) if p != color])
                
        return min(mc)
