from typing import List


class Solution:

    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        sublist_up = [0 for _ in range(len(security))]
        sublist_down = [0 for _ in range(len(security))]
        for i in range(1, len(security)):
            if security[i] <= security[i - 1]:
                sublist_down[i] = sublist_down[i - 1] + 1
            else:
                sublist_down[i] = 0
        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i + 1]:
                sublist_up[i] = sublist_up[i + 1] + 1
            else:
                sublist_up[i] = 0
        ans = []
        for i in range(len(security)):
            if sublist_down[i] >= time and sublist_up[i] >= time:
                ans.append(i)
        return ans

def main():
    print(Solution().goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2))

if __name__ == "__main__":
    main()