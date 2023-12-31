from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(x: int, y: int, gold: int, h: set) -> int:
            direction = [[0, -1], [-1, 0], [1, 0], [0, 1]]
            if (x, y) in h or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return gold
            h.add((x, y))
            gold += grid[x][y]
            ans = max([dfs(x + d[0], y + d[1], gold, h) for d in direction])
            h.remove((x, y))
            return ans

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j, 0, set()))
        return ans

def main():
    print(Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))

if __name__ == "__main__":
    main()