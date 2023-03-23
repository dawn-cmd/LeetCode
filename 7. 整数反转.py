class Solution:
    def reverse(self, x: int) -> int:
        c, x = (-1, -x) if x < 0 else (1, x)
        x = list(str(x))
        x.reverse()
        x = int(''.join(x)) * c
        return x if -2 ** 31 <= x <= (2 ** 31) - 1 else 0

def main():
    print(Solution().reverse(-1200))

if __name__ == "__main__":
    main()
