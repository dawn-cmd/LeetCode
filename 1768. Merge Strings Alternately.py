"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
链接：https://leetcode.cn/problems/merge-strings-alternately
"""


class Solution:
    """
    Solution
    """
    
    @staticmethod
    def mergeAlternately(word1: str, word2: str) -> str:
        """
        mergeAlternately
        """
        ans = "".join([word1[_] + word2[_] for _ in range(min(len(word1), len(word2)))])
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        ans += word1[len(word2):]
        return ans


print(Solution().mergeAlternately(word1="abc", word2="pqr"))
