class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ""
        for i in range(numRows):
            for j in range(i, len(s), numRows * 2 - 2):
                ans += s[j]
                if i == 0 or i == numRows - 1:
                    continue
                if j + 2 * numRows - 2 * i - 2 < len(s):
                    ans += s[j + 2 * numRows - 2 * i - 2]
        return ans

def main():
    print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))

if __name__ == "__main__":
    main()