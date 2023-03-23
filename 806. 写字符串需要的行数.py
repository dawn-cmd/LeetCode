from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        rest = 100
        for c in s:
            wid = widths[ord(c) - ord('a')]
            if rest < wid:
                lines += 1
                rest = 100 - wid
            else:
                rest -= wid
        return [lines, 100 - rest]

def main():
    print(Solution().numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))

if __name__ == "__main__":
    main()
