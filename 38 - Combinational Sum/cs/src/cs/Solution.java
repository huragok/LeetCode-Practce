package cs;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        int n = candidates.length;
        List<Integer> candidateArray = new ArrayList<Integer> (n);
        for (int i = 0; i < n; i++) {
        	candidateArray.add(candidates[i]);
        }
        
        return combinationSumPartial(candidateArray, target);
    }
    
    private List<List<Integer>> combinationSumPartial(List<Integer> candidates, int target) {

    	int n = candidates.size();
    	if (target == 0) {
			List<List<Integer>> result = new ArrayList<List<Integer>>(1);
			List<Integer> entry = new ArrayList<Integer>(1);
			result.add(entry);
			return result;
		} else if (n == 0) {
			return new ArrayList<List<Integer>>(1);
    	} else {
    		int v = candidates.get(0);
    		if (v > target) {
    			return new ArrayList<List<Integer>>(1);
    		} else {
    			List<List<Integer>> results = combinationSumPartial(candidates.subList(1, n), target);
    			List<List<Integer>> resultsPartialInclude = combinationSumPartial(candidates, target - v);
    			
    			for (List<Integer> entry: resultsPartialInclude) {
    				entry.add(0, v);
    			}
    			results.addAll(resultsPartialInclude);
    			return results;
    		}
    	}
    }
    
    public static void main(String [] args) {
    	int [] candidates = new int [] {2,3,6,7};
    	int target = 7;
    	
    	System.out.println(new Solution().combinationSum(candidates, target));
    }
}
