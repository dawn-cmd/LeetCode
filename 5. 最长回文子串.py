from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + ''.join([_ + '#' for _ in s])
        length = [0 for _ in range(len(s))]
        right = 0
        j = 0

        def expand(now: int, length: List[int]):
            l = now - length[now]
            r = now + length[now]
            while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
                length[now] += 1

        max_id = 0
        max_length = 0
        for i in range(1, len(s)):
            if i <= right:
                length[i] = min(length[2 * j - i], right - i)
            expand(i, length)
            if i + length[i] > right:
                right = i + length[i]
                j = i
            if length[i] > max_length:
                max_length = length[i]
                max_id = i
        ans = s[max_id - max_length:max_id + max_length + 1].replace('#', '')
        return ans


def main():
    print(Solution().longestPalindrome(s = "babadada"))

if __name__ == "__main__":
    main()