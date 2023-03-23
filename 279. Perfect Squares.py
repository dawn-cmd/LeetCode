class Solution:
    def numSquares(self, n: int) -> int:
        ps = set([i * i for i in range(1, int(n**0.5)+1)])

        def divisible(n, count):
            if count == 1: return n in ps
            for p in ps:
                if divisible(n-p, count-1):
                    return True
            return False

        for count in range(1, n+1):
            if divisible(n, count):
                return count

print(Solution().numSquares(12))
