from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        cnts = [0 for _ in range(numCourses)]
        h = [0 for _ in range(numCourses)]
        for p in prerequisites:
            cnts[p[0]] += 1
            g[p[1]].append(p[0])
        while True:
            change = False
            for i in range(len(cnts)):
                if cnts[i] > 0 or h[i] == 1:
                    continue
                change = True
                h[i] = 1
                for j in range(len(g[i])):
                    cnts[g[i][j]] -= 1
            if change == False:
                break
        for i in range(len(h)):
            if h[i] == 0:
                return False
        return True

print(Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
