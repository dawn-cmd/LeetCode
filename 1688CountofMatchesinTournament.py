class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
    
def main():
    solution = Solution()
    print(solution.numberOfMatches(14))

if __name__ == "__main__":
    main()