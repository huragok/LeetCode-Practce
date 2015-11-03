package cs2;

import java.util.Collections;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Map<Integer, Integer> count = new HashMap<Integer, Integer> ();
        for (int i = 0; i < candidates.length; i++) {
        	if (!count .containsKey(candidates[i])) {
        		count .put(candidates[i], 1);
        	} else {
        		count .put(candidates[i], count .get(candidates[i]) + 1);
        	}
        }
        Set<Integer> numsSet = count .keySet();
        List<Integer> numsList = new ArrayList<Integer> ();
        numsList.addAll(numsSet);
        Collections.sort(numsList);

        return combinationSum2(numsList, target, count);
    }
    
    private List<List<Integer>> combinationSum2(List<Integer> nums, int target, Map<Integer, Integer> count) {
    	List<List<Integer>> result = new ArrayList<List<Integer>> ();
    	if (target == 0) {
    		result.add(new ArrayList<Integer> ());
  
    	} else {
    		int n = nums.size();
    		if (n > 0) {
    			int v = nums.get(0);
    			if (v <= target) {
    				int iMax = target / v > count.get(v) ? count.get(v) : target / v;
    				
    				for (int i = 0; i <= iMax; i++) {
    					List<List<Integer>> resultPartial = combinationSum2(nums.subList(1,  n), target - i * v, count);
    					for (List<Integer> entry: resultPartial) {
    						for (int j = 0; j < i; j++) {
    							
    							entry.add(0, v);
    						}
    					}

    					result.addAll(resultPartial);
    				}
    				return result;
    			}
    		}
    	}
  		return result;
    }
    
    public static void main(String [] args) {
    	int [] candidates = new int [] {10,1,2,7,6,1,5};
    	int target = 8;
    	
    	System.out.println(new Solution().combinationSum2(candidates, target));
    }
}