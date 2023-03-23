from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = s1.split() + s2.split()
        return [s for s in s3 if s3.count(s) == 1]

def main():
    solution = Solution()
    print(solution.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))

if __name__ == "__main__":
    main()