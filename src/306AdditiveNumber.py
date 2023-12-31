class Solution:
    def check(self, a: int, b: int, rest: str) -> bool:
        for i in range(1, len(rest) + 1):
            if a + b == int(rest[:i]):
                if i == len(rest):
                    return True
                else:
                    if rest[i] == '0':
                        return False
                    return self.check(b, int(rest[:i]), rest[i:])
        return False

    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num) - 1):
            if i > 1 and num[0] == '0':
                continue
            for j in range(i + 1, len(num)):
                if j > i + 1 and num[i] == '0':
                    continue
                if len(num[j:]) > 1 and num[j] == '0':
                    continue
                if self.check(int(num[:i]), int(num[i:j]), num[j:]):
                    return True
        return False

def main():
    solution = Solution()
    num = input()
    print(solution.isAdditiveNumber(num))

if __name__ == "__main__":
    main()
