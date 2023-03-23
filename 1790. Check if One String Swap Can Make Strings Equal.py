class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        for l in range(1, len(s1) // 2 + 1):
            for i in range(0, len(s1) - l):
                for j in range(i + l, len(s1)):
                    if s1[:i] + s1[j:j + l] + s1[i + l:j] + s1[i:i + l] + s1[j + l:] == s2:
                        return True
        return False


def main():
    print(Solution().areAlmostEqual(s1="bank", s2="kanb"))


if __name__ == '__main__':
    main()
