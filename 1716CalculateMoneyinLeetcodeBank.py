class Solution:
    def totalMoney(self, n: int) -> int:
        return sum([sum([j + i + 1 for j in range(min(7, n - i * 7))]) for i in range(n // 7 + 1)])
    
def main():
    solution = Solution()
    print(solution.totalMoney(20))

if __name__ == "__main__":
    main()