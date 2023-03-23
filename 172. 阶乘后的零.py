from functools import reduce


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        ans = str(reduce(lambda x, y: x * y, range(1, n + 1)))
        id = len(ans) - 1
        while ans[id] == '0' and id > 0:
            id -= 1
        return len(ans) - id - 1

def main():
    print(Solution().trailingZeroes(100))

if __name__ == "__main__":
    main()
