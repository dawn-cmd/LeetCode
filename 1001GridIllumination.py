from collections import Counter
from typing import List


class Solution:

    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps = set([(x[0], x[1]) for x in lamps])
        row, line, diagonal, anti_diagonal = Counter(), Counter(), Counter(), Counter()
        for lamp in lamps:
            row[lamp[0]] += 1
            line[lamp[1]] += 1
            diagonal[lamp[0] + lamp[1]] += 1
            anti_diagonal[lamp[0] - lamp[1]] += 1
        ans = []
        directions = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for query in queries:
            if (query[0], query[1]) in lamps or row[query[0]] > 0 or line[query[1]] > 0 or diagonal[query[0] + query[1]] > 0 or anti_diagonal[query[0] - query[1]] > 0:
                ans.append(1)
            else:
                ans.append(0)
            for d in directions:
                if (query[0] + d[0], query[1] + d[1]) not in lamps:
                    continue
                lamps.remove((query[0] + d[0], query[1] + d[1]))
                row[query[0] + d[0]] -= 1
                line[query[1] + d[1]] -= 1
                diagonal[query[0] + d[0] + query[1] + d[1]] -= 1
                anti_diagonal[query[0] + d[0] - query[1] - d[1]] -= 1
        return ans

def main():
    print(Solution().gridIllumination(n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]))

if __name__ == "__main__":
    main()