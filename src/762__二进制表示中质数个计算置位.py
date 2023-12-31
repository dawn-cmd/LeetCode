class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def is_prime(n: int) -> bool:
            if n == 0 or n == 1:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        ans = 0
        for i in range(left, right + 1):
            cnt = 0
            n = i
            while n:
                cnt += n % 2
                n //= 2
            if is_prime(cnt):
                ans += 1
        return ans
    
def main():
    print(Solution().countPrimeSetBits(6, 10))

if __name__ == "__main__":
    main()
