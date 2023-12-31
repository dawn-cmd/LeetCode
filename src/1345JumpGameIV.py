from collections import defaultdict, deque
from email.policy import default
from re import S
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:  # special judge
            return 0

        graph = defaultdict(list)
        for i in range(len(arr)):
            graph[arr[i]].append(i)
        # build arr into a graph

        q = deque([(0, 0)])  # use tuple to record position and steps (like (pos, step))
        h = set([0])
        while q:
            pos, step = q.popleft()
            for i in graph[arr[pos]]:
                if i in h:  # head back
                    continue
                if i == len(arr) - 1:  # find the end, then return
                    return step + 1
                q.append((i, step + 1))
                h.add(i)
            del graph[arr[pos]]
            if pos - 1 >= 0 and (pos - 1) not in h:
                q.append((pos - 1, step + 1))
                h.add(pos - 1)
            if pos + 1 < len(arr) and (pos + 1) not in h:
                if pos + 1 == len(arr) - 1:
                    return step + 1
                q.append((pos + 1, step + 1))
                h.add(pos + 1)
        # use dfs to get the shortest path

        return -1

def main():
    solution = Solution()
    print(solution.minJumps([11,22,7,7,7,7,7,7,7,22,13]))

if __name__ == "__main__":
    main()
