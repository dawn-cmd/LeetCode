from tkinter import SOLID
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def getcode(num: int) -> str:
            ans = str(bin(num))[2:]
            while len(ans) < 8:
                ans = '0' + ans
            return ans
        
        data = [getcode(_) for _ in data]

        def check_head(num: str) -> int:
            if '0' not in num:
                return -1
            if num[0] == '0':
                return 1
            cnt = 0
            while num[cnt] == '1' and cnt < len(num):
                cnt += 1
            if cnt == 1:
                return -1
            else:
                return cnt
        
        id = 0
        while id < len(data):
            cnt = check_head(data[id])
            if cnt == -1:
                return False
            if cnt > 4:
                return False
            if cnt == 1:
                id += 1
                continue
            if len(data) - id < cnt:
                return False
            for i in range(id + 1, id + cnt):
                if data[i][:2] != "10":
                    return False
            id += cnt
        return True

def main():
    print(Solution().validUtf8(data = [250,145,145,145,145]))

if __name__ == "__main__":
    main()