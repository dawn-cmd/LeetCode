from collections import deque
from functools import cmp_to_key
from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 3:
            return trees
            
        def cross(a: List[int], b: List[int], c: List[int]) -> int:
            return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

        def dis(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        buttom = 0
        for i in range(len(trees)):
            if trees[i][1] < trees[buttom][1]:
                buttom = i
        trees[0], trees[buttom] = trees[buttom], trees[0]

        def cmp(a: List[int], b: List[int]):
            if cross(trees[0], a, b) == 0:
                return dis(a, trees[0]) - dis(b, trees[0])
            else:
                return cross(trees[0], b, a)

        trees[1:] = sorted(trees[1:], key=cmp_to_key(cmp))
        id = len(trees)
        for i in range(len(trees) - 2, -1, -1):
            if cross(trees[0], trees[len(trees) - 1], trees[i]) != 0:
                break
            id = i
        trees[id:] = sorted(trees[id:], key=lambda x: -dis(x, trees[0]))
        q = deque([trees[0], trees[1]])
        for i in range(2, len(trees)):
            while len(q) > 1 and cross(q[-2], trees[i], q[-1]) > 0:
                q.pop()
            q.append(trees[i])
        return list(q) 

def main():
    print(Solution().outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))

if __name__ == "__main__":
    main()
