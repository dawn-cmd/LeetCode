class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def match_character(c: str) -> str:
            return c.upper() if 'a' <= c <= 'z' else c.lower()

        def check_str(s: str) -> bool:
            d = set(s)
            for c in d:
                if match_character(c) not in d:
                    return False
            return True
        
        for length in range(len(s), 0, -1):
            for st in range(len(s) - length + 1):
                if check_str(s[st:st + length]):
                    return s[st:st + length]
        return ""

def main():
    print(Solution().longestNiceSubstring("dDzeE"))

if __name__ == "__main__":
    main()