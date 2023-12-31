from typing import List


class Solution:
    
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        prefix = [0 if s[0] == '*' else 1]
        for i in range(1, len(s)):
            prefix.append(prefix[i - 1] + (0 if s[i] == '*' else 1))
        close_candle_left = [0 for _ in range(len(s))]
        mark = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '|':
                mark = i
            close_candle_left[i] = mark
        close_candle_right = [0 for _ in range(len(s))]
        mark = -1
        for i in range(len(s)):
            if s[i] == '|':
                mark = i
            close_candle_right[i] = mark
        for query in queries:
            if close_candle_left[query[0]] == -1 or close_candle_right[query[1]] == -1:
                ans.append(0)
                continue
            if close_candle_left[query[0]] > query[1] or close_candle_right[query[1]] < query[0]:
                ans.append(0)
                continue
            cnt = query[1] - query[0] + 1
            cnt -= close_candle_left[query[0]] - query[0]
            cnt -= query[1] - close_candle_right[query[1]]                     
            cnt -= prefix[query[1]] - (0 if query[0] == 0 else prefix[query[0] - 1])
            ans.append(cnt)
        return ans

def main():
    print(Solution().platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]]))

if __name__ == "__main__":
    main()