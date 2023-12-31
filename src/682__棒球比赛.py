from collections import deque
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = deque()
        for op in ops:
            if op == 'C':
                stk.pop()
            elif op == 'D':
                stk.append(stk[-1] * 2)
            elif op == '+':
                stk.append(stk[-1] + stk[-2])
            else:
                stk.append(int(op))
        return sum(stk)

def main():
    print(Solution().calPoints(ops = ["5","-2","4","C","D","9","+","+"]))

if __name__ == "__main__":
    main()
