class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_freq = 0
        frequence = [0] * 26
        res = 0
        while right < len(s):
            frequence[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, frequence[ord(s[right]) - ord('A')])
            right += 1
            if right - left > max_freq + k:
                frequence[ord(s[left]) - ord('A')] -= 1
                left += 1
            res = max(res, right - left)
        return res
