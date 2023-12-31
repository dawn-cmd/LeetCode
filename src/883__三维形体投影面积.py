from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        ans += sum(grid[i][j] > 0 for i in range(len(grid)) for j in range(len(grid)))
        ans += sum([max(row) for row in grid])
        ans += sum([max(col) for col in zip(*grid)])
        return ans
def main():
    print(Solution().projectionArea([[1,0],[0,2]]))

if __name__ == "__main__":
    main()
