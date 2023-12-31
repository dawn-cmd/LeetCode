from collections import deque
from unicodedata import name


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        h = set()
        max_length = 0
        for i in range(len(s)):
            while s[i] in h:
                h.remove(q.pop())
            q.appendleft(s[i])
            h.add(s[i])
            max_length = max(max_length, len(q))
        return max_length

def main():
    print(Solution().lengthOfLongestSubstring(s = "pwwkew"))

if __name__ == "__main__":
    main()