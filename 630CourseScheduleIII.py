from typing import List
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = [course for course in courses if course[0] <= course[1]]
        courses.sort(key=lambda a: a[1])
        q = list()
        tot = 0 
        for course in courses:
            if tot + course[0] <= course[1]:
                heapq.heappush(q, -course[0])
                tot += course[0]
            elif q and course[0] < -q[0]:
                tot = tot - (-q[0]) + course[0]
                heapq.heappop(q)
                heapq.heappush(q, -course[0])
        return len(q)

def main():
    solution = Solution()
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print(solution.scheduleCourse(courses))

if __name__ == "__main__":
    main()