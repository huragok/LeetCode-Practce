class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        residual = 0
        min_residual = 0
        pos_min_residual = 0
        for i in range(1, n):
            residual += gas[i - 1] - cost[i - 1]
            if residual < min_residual:
                min_residual = residual
                pos_min_residual = i
            
        residual += gas[n - 1] - cost[n - 1]
        return -1 if residual < 0 else pos_min_residual
