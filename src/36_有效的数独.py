from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        sqr = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = 1 << int(board[i][j])
                if num & row[i] != 0:
                    return False
                if num & col[j] != 0:
                    return False
                if num & sqr[i // 3 * 3 + j // 3] != 0:
                    return False
                row[i] |= num
                col[j] |= num
                sqr[i // 3 * 3 + j // 3] |= num
        return True
