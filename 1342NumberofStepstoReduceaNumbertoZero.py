class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            ans += 1
        return ans

def main():
    print(Solution().numberOfSteps(123))

if __name__ == "__main__":
    main()