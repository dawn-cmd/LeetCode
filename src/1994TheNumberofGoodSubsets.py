from collections import Counter
from typing import List


class Solution:
    
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        nums = [x for x in nums if x % 4 and x % 9 and x % 25]
        freq = Counter(nums)
        mod = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        f = [0] * (1 << len(primes))
        f[0] = pow(2, freq[1], mod)
        for i, occ in freq.items():
            if i == 1:
                continue
            subset = 0
            for j in range(len(primes)):
                if i % primes[j] == 0:
                    subset |= (1 << j)
            for mask in range((1 << len(primes)) - 1, 0, -1):
                if mask & subset == subset:
                    f[mask] = (f[mask] + f[mask ^ subset] * freq[i]) % mod
        ans = sum(f[1:]) % mod
        return ans

def main():
    print(Solution().numberOfGoodSubsets([6,8,1,8,6,5,6,11,17]))

if __name__ == "__main__":
    main()