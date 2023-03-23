from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        existType = []
        lastAppear = {}
        cnt = 0
        ans = 0
        for i in range(len(fruits)):
            # print(existType)
            lastAppear[fruits[i]] = i
            if fruits[i] in existType:
                cnt += 1
                continue
            if len(existType) < 2:
                existType.append(fruits[i])
                cnt += 1
                continue
            if lastAppear[existType[0]] < lastAppear[existType[1]]:
                existType[0], existType[1] = existType[1], existType[0]
            ans = max(ans, cnt)
            cnt -= lastAppear[existType[1]] - (i - 1 - cnt + 1) + 1
            existType.pop()
            existType.append(fruits[i])
            cnt += 1
        ans = max(ans, cnt)
        return ans
    

print(Solution().totalFruit([0, 1, 2, 2]))