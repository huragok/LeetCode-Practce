package cs2;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	
	private List<List<Integer>> prerequisitesList;
	private int count;
	private int [] schedule;
	private int [] visited;
	
	public int[] findOrder(int numCourses, int[][] prerequisites) {
		if (numCourses < 1) return new int [0];
		
		// Initialization
		prerequisitesList = new ArrayList<List<Integer>> (numCourses);
		for (int i = 0; i < numCourses; i++) prerequisitesList.add(new ArrayList<Integer> ());
		for (int i = 0; i < prerequisites.length; i++) {
			prerequisitesList.get(prerequisites[i][0]).add(prerequisites[i][1]);
		}
		
		count = 0;
		schedule = new int [numCourses];
		visited = new int [numCourses];
		
		for (int i = 0; i < numCourses; i++) {
			if (!dfs(i)) return new int [0];
		}
		
		return schedule;
    }
	
	private boolean dfs(int course) {
		if (visited[course] == 2) {
			return true;
		} else if (visited[course] == 1) {
			return false;
		} else {
			visited[course] = 1;
			for (int prereq: prerequisitesList.get(course)) {
				if (!dfs(prereq)) return false;
			}
			visited[course] = 2;
			schedule[count] = course;
			count++;
			return true;
		}
	}
}
