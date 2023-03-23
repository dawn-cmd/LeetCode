from typing import List


class Solution:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = set()
        for word in words:
            tmp = ""
            for c in word:
                tmp += self.morse[ord(c) - ord('a')]
            ans.add(tmp)
        return len(ans)

def main():
    print(Solution().uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"]))

if __name__ == "__main__":
    main()
