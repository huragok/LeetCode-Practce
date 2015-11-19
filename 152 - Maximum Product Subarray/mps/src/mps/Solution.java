package mps;

public class Solution {
	public int maxProduct(int[] nums) {
       int n = nums.length;
       if (n == 1) return nums[0]; 
       int maxPos = 0, minNeg = 0;
       int maxPosNew, minNegNew;
       int productMax = nums[0];

       for (int num: nums) {
    	   if (num > 0) {
    		   if (maxPos == 0) {
    			   maxPosNew = num;
    		   } else {
    			   maxPosNew = maxPos * num;
    		   }
    		   
    		   minNegNew = minNeg * num;
    	   } else if (num < 0) {
    		   if (maxPos == 0) {
    			   minNegNew = num;
    		   } else {
    			   minNegNew = maxPos * num;
    		   }
    		   maxPosNew = minNeg * num;
    		   
    	   } else {
    		   maxPosNew = 0;
    		   minNegNew = 0;
    	   }
    	   maxPos = maxPosNew; minNeg = minNegNew;
    	   //System.out.println(maxPos); System.out.println(minNeg);
    	   //System.out.println("_____");
    	   
    	   if (maxPos > productMax) {
    		   productMax = maxPos;
    	   }
       }
       return productMax;
    }
}
