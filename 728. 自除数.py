from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        def check(n: int) -> bool:
            for i in str(n):
                if i == '0':
                    return False
                if n % int(i) != 0:
                    return False
            return True

        for i in range(left, right + 1):
            if check(i):
                ans.append(i)
        return ans

def main():
    print(Solution().selfDividingNumbers(1, 10000))

if __name__ == "__main__":
    main()
