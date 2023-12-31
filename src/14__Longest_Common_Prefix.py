from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            tmp = ""
            for j in range(min(len(ans), len(strs[i]))):
                if ans[j] == strs[i][j]:
                    tmp += ans[j]
                else:
                    break
            ans = tmp
        return ans
    
def main():
    print(Solution().longestCommonPrefix(strs = ["flower","flow","flight"]))

if __name__ == "__main__":
    main()
