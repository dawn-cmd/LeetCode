from typing import List
import heapq


class Solution:
    def getID(self, x: int, y: int, grid: List[List[int]]) -> int:
        return x * len(grid[0]) + y
    
    def getPos(self, id: int, grid: List[List[int]]) -> tuple[int, int]:
        return (id // len(grid[0]), id % len(grid[0]))

    def dijkstra(self, grid: List[List[int]]) -> int:
        q = []
        heapq.heappush((0, 0))

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        