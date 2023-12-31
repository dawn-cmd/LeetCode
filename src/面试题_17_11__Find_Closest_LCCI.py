from cmath import inf
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        last_word = ''
        last_id = -1
        min_d = inf
        for i, word in enumerate(words):
            if word != word1 and word != word2:
                continue
            if last_word == '':
                last_word, last_id = word, i
                continue
            if last_word == word:
                last_id = i
                continue
            min_d = min(min_d, i - last_id)
            last_word, last_id = word, i
            if min_d == 1:
                break
        return min_d

def main():
    print(Solution().findClosest(words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"))

if __name__ == "__main__":
    main()
