from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        index_set = set()
        for pos in positions:
            index_set.add(pos[0])
            index_set.add(pos[0] + pos[1] - 1)
        index_set = sorted(list(index_set))
        index_map = {val: index for index, val in enumerate(index_set)}
        ans = []
        heights = [0 for _ in range(len(index_set))]
        max_height = 0
        for pos in positions:
            x, y = index_map[pos[0]], index_map[pos[0] + pos[1] - 1]
            cur_h = max(heights[x : y + 1]) + pos[1]
            for indx in range(x, y + 1):
                heights[indx] = cur_h
            max_height = max(max_height, cur_h)
            ans.append(max_height)
        return ans

def main():
    print(Solution().fallingSquares(positions = [[1,2],[2,3],[6,1]]))

if __name__ == "__main__":
    main()
