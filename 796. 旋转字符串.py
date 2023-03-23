class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

def main():
    print(Solution().rotateString(s = "abcde", goal = "abced"))

if  __name__ == "__main__":
    main()
