from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ""
        d = set()
        for word in words:
            if len(word) == 1 or word[:-1] in d:
                d.add(word)
                ans = word if len(word) > len(ans) else ans
        return ans

def main():
    print(Solution().longestWord(words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]))

if __name__ == "__main__":
    main()
