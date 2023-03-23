class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = list(sentence.split())
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if s[i][0] in vowel:
                s[i] += 'ma'
            else:
                s[i] = s[i][1:] + s[i][0] + 'ma'
            for j in range(i + 1):
                s[i] += 'a'
        return ' '.join(s)

def main():
    print(Solution().toGoatLatin(sentence = "I speak Goat Latin"))

if __name__ == "__main__":
    main()
