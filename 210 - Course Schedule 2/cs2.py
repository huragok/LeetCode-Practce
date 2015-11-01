class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        self.prereq = [set() for course in range(numCourses)]
        for p in prerequisites:
            self.prereq[p[0]].add(p[1])
        self.color = [0] * numCourses
        self.order = []
        
        for course in range(numCourses):
            if self.color[course] == 0:
                if not self.dfsVisit(course):
                    return []
        return self.order
        
    def dfsVisit(self, course):
        self.color[course] = 1
        for course_prereq in self.prereq[course]:
            if self.color[course_prereq] == 1:
                return False
            elif self.color[course_prereq] == 0:
                if not self.dfsVisit(course_prereq):
                    return False
                    
        self.color[course] = 2
        self.order.append(course)
        return True
        
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(Solution().findOrder(numCourses, prerequisites))
