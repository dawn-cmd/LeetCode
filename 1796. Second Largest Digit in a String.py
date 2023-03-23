class Solution:
    def secondHighest(self, s: str) -> int:
        num = [int(s[_]) for _ in range(len(s)) if s[_].isdigit()]
        num.sort()
        for i in range(len(num) - 1, 0, -1):
            if num[i] != num[i - 1]:
                return num[i - 1]
        return -1
        
def main():
    s = input()
    print(Solution().secondHighest(s))

if __name__ == '__main__':
    main()
        