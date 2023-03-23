from typing import List


class Solution:

    def gcd(self, a: int, b: int):
        return a if b == 0 else self.gcd(b, a % b)
    
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if self.gcd(i, j) == 1:
                    ans.append(f"{j}/{i}")
        return ans

def main():
    print(Solution().simplifiedFractions(1))

if __name__ == "__main__":
    main()
