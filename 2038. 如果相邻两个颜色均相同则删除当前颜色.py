class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt_a, cnt_b = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    cnt_a += 1
                else:
                    cnt_b += 1
        return False if cnt_b >= cnt_a else True
