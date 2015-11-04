package p;

import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
    	List<Integer> numsList= new ArrayList<Integer> (nums.length);
    	for (int i = 0; i < nums.length; i++) {
    		numsList.add(nums[i]);
    	}
    	return permutePartial(numsList);
    }
    
    private List<List<Integer>> permutePartial(List<Integer> partial) {
    	
    	int n = partial.size();
    	List<List<Integer>> result = new ArrayList<List<Integer>> ();
    	
    	if (n == 1) {
    		List<Integer> entry = new ArrayList<Integer> (1);
    		entry.add(partial.get(0));
    		result.add(entry);
    		return result;
    	} else {
    		for (int i = 0; i < n; i++){
    			List<Integer> partialNew = new ArrayList<Integer>(partial.subList(0, i));
    			partialNew.addAll(partial.subList(i + 1, n));
    			
    			List<List<Integer>> resultPartial = permutePartial(partialNew);
    			for (List<Integer> l: resultPartial) {
    				l.add(0, partial.get(i));
    			}
    			result.addAll(resultPartial);
    		}
    		return result;
    	}
    	
    }
    
    public static void main(String [] args) {
    	int [] nums = {1,2,3};
    	System.out.println(new Solution().permute(nums));
    }
}
