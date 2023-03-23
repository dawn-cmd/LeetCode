class Solution:
    
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))

def main():
    print(Solution().findLUSlength(a = "aba", b = "cdc"))

if __name__ == "__main__":
    main()