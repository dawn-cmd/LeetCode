from typing import List
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cub in cuboids:
            cub.sort(key=lambda x: -x)
        cuboids.sort(key=lambda x: -sum(x))
        print(cuboids)
        dp = [_[0] for _ in cuboids]
        ans = dp[0]
        for i in range(1, len(cuboids)):
            for j in range(i):
                if cuboids[i][0] <= cuboids[j][0] and cuboids[i][1] <= cuboids[j][1] and cuboids[i][2] <= cuboids[j][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][0])
            ans = max(ans, dp[i])
        return ans
    
if __name__ == '__main__':
    print(Solution().maxHeight([[50,45,20],[95,37,53],[45,23,12]]))