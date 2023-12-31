from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = -1
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    xa, xb, ya, yb, za, zb = points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]
                    ans = max(ans, 0.5 * abs(xa * yb + ya * zb + za * xb - xa * zb - ya * xb - za * yb))
        return ans

def main():
    print(Solution().largestTriangleArea(points = [[0,0],[0,1],[1,0],[0,2],[2,0]]))

if __name__ == "__main__":
    main()
