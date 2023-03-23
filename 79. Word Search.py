from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(h: List[List[bool]], now: List[int], rest: str) -> bool:
            if rest == "":
                return True
            if h[now[0]][now[1]] or rest[0] != board[now[0]][now[1]]:
                return False
            if len(rest) == 1 and board[now[0]][now[1]] == rest:
                return True
            h[now[0]][now[1]] = True
            dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            ans = False
            for dir in dirs:
                if not (0 <= (now[0] + dir[0]) < len(board) and 0 <= (now[1] + dir[1]) < len(board[0])):
                    continue
                ans = ans or dfs(h, [now[0] + dir[0], now[1] + dir[1]], rest[1:])
                if ans:
                    break
            h[now[0]][now[1]] = False
            return ans
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and dfs(h, [i, j], word):
                    return True
        return False

print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
