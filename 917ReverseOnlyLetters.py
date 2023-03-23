class Solution:
    
    def reverseOnlyLetters(self, s: str) -> str:
        tmp = [x for x in s if 'a' <= x <= 'z' or 'A' <= x <= 'Z']
        tmp.reverse()
        id = 0
        s = list(s)
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
                s[i] = tmp[id]
                id += 1
        return ''.join(s)

def main():
    print(Solution().reverseOnlyLetters(s = "Test1ng-Leet=code-Q!"))

if __name__ == "__main__":
    main()