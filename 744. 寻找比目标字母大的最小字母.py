from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = set(letters)
        min_dif = 1e5
        ans = ''
        for letter in letters:
            if letter > target:
                if ord(letter) - ord(target) < min_dif:
                    min_dif = ord(letter) - ord(target)
                    ans = letter
            else:
                if ord(letter) + 26 - ord(target) < min_dif:
                    min_dif = ord(letter) + 26 - ord(target)
                    ans = letter
        return ans

def main():
    print(Solution().nextGreatestLetter(letters = ["c", "f", "j"], target = "a"))

if __name__ == "__main__":
    main()
