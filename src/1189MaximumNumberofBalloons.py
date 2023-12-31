from collections import Counter


class Solution:
    
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        return min(cnt['b'], cnt['a'], cnt['l'] // 2, cnt['o'] // 2, cnt['n'])

def main():
    print(Solution().maxNumberOfBalloons(text = "loonbalxballpoon"))

if __name__ == "__main__":
    main()