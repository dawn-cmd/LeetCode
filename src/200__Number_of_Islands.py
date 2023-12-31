from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = int(grid[i][j])
        grid = [[0 for _ in range(len(grid[0]))]] + grid + [[0 for _ in range(len(grid[0]))]]
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        # print(grid)
        h = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]

        def bfs(x: int, y: int, h: List[List[int]]):
            if grid[x][y] == 0 or h[x][y] == 1:
                return
            st = deque()
            h[x][y] = 1
            st.append((x, y))
            directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while st:
                # print(st[0])
                for d in directs:
                    x1 = st[0][0] + d[0]
                    y1 = st[0][1] + d[1]
                    if (grid[x1][y1] == 0) or (h[x1][y1] == 1):
                        continue
                    # print(x1, y1)
                    # print("passed")
                    st.append((x1, y1))
                    h[x1][y1] = 1
                    # print(h)
                st.popleft()

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0 or h[i][j] == 1:
                    continue
                bfs(i, j, h)
                ans += 1
        return ans    


print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
