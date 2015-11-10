package lcs;

import java.util.Set;
import java.util.HashSet;

public class Solution {
	public int longestConsecutive(int[] nums) {
        Set<Integer> numsSet = new HashSet<Integer> ();
        for (int num: nums) numsSet.add(num);
        
        int lenConsecMax = 0;
        for (int num: numsSet) {
        	if (!numsSet.contains(num - 1)) {
        		int tailConsec = num;
        		while (numsSet.contains(tailConsec)) {
        			tailConsec++;
        		}
        		
        		if (tailConsec - num > lenConsecMax) lenConsecMax = tailConsec - num;
        	}
        }
        return lenConsecMax;
    }
}
