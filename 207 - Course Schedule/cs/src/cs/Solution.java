package cs;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	private int [] visited; // 0 means not visited, 1 means on hold, 2 means visited in the dfs
	private List<List<Integer>> prerequisitesList;
	
	public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses < 1) return true;
        
        visited = new int [numCourses]; 
        prerequisitesList = new ArrayList<List<Integer>> (numCourses);
        for (int i = 0; i < numCourses; i++) prerequisitesList.add(new ArrayList<Integer> ());
        
        for (int i = 0; i < prerequisites.length; i++) {
        	prerequisitesList.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }
        
        for (int i = 0; i < numCourses; i++) {
        	visited[i] = 0;
        }
        
        for (int i = 0; i < numCourses; i++) {
        	if (!dfs(i)) return false;
        }
        return true;
    }
	
	private boolean dfs(int course) {
		if (visited[course] == 2) {
			return true;
		} else if (visited[course] == 1) {
			return false;
		} else {
			visited[course] = 1;
			for (int prereq: prerequisitesList.get(course)) {
				boolean canTake = dfs(prereq);
				if (!canTake) return false;
			}
			visited[course] = 2;
		}
		return true;
	}
}
