class Solution:

    def reversePrefix(self, word: str, ch: str) -> str:
        id = word.find(ch)
        if id == -1:
            return word
        return word[id::-1] + word[id + 1:]

def main():
    print(Solution().reversePrefix(word = "abcdefd", ch = "d"))

if __name__ == "__main__":
    main()