from bisect import bisect, bisect_left


class Solution:

    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1, 1]
        while f[-1] < k:
            f.append(f[-1] + f[-2])
        cnt = 0
        while k > 0:
            tmp = bisect_left(f, k)
            k = k - f[tmp - 1] if f[tmp] > k else 0
            cnt += 1
        return cnt
    
def main():
    print(Solution().findMinFibonacciNumbers(19))

if __name__ == "__main__":
    main()