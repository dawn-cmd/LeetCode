class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getcnt(x: int, limit: int) -> int:
            ans, cnt = 0, 1
            for i in range(len(str(limit)) - len(str(x))):
                ans += cnt
                cnt *= 10
            u = int(str(limit)[:len(str(x))])
            if u > x:
                ans += cnt
            elif u == x:
                ans += limit - x * cnt + 1
            return ans

        ans = 1
        while k > 1:
            cnt = getcnt(ans, n)
            if k > cnt:
                ans += 1
                k -= cnt
            else:
                k -= 1
                ans *= 10
        return ans

def main():
    print(Solution().findKthNumber(1000, 4))

if __name__ == "__main__":
    main()
