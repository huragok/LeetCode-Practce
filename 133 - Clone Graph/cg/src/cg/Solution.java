package cg;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class Solution {
	class UndirectedGraphNode {
		int label;
		List<UndirectedGraphNode> neighbors;
		UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
	};
		 
	public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;
		Map<Integer, UndirectedGraphNode> nodesNew = new HashMap<Integer, UndirectedGraphNode> ();
		Queue<UndirectedGraphNode> q = new LinkedList<UndirectedGraphNode> ();
		q.add(node);
		
		// BFS
		while (!q.isEmpty()) {
			UndirectedGraphNode nodeToCopy = q.poll();
			UndirectedGraphNode nodeNew;
			if (!nodesNew.containsKey(nodeToCopy.label)) {
				nodeNew = new UndirectedGraphNode(nodeToCopy.label);
				nodesNew.put(nodeToCopy.label, nodeNew);
			}
			nodeNew = nodesNew.get(nodeToCopy.label);
			
			for (UndirectedGraphNode neighbor: nodeToCopy.neighbors) {
				if (!nodesNew.containsKey(neighbor.label)) {
					q.add(neighbor);
					UndirectedGraphNode neighborNew = new UndirectedGraphNode(neighbor.label);
					nodesNew.put(neighbor.label, neighborNew);
				}
				nodeNew.neighbors.add(nodesNew.get(neighbor.label));
			}
		}
		
		return nodesNew.get(node.label);
    }
}
