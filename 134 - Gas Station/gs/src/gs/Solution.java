package gs;

public class Solution {
	public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int residual = gas[0] - cost[0];
        int minResidual = residual;
        int start = 0;
        
        for (int i = 1; i < n; i++) {
        	residual += gas[i] - cost[i];
        	if (residual < minResidual) {
        		minResidual = residual;
        		start = i;
        	}
        }
        if (residual < 0) {
        	return -1;
        } else {
        	return (start + 1) % n;
        }
    }
}
