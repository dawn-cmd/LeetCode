class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False
        elif len(first) == len(second):
            cnt = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    cnt += 1
                if cnt > 1:
                    return False
            return True
        else:
            if len(first) < len(second):
                first, second = second, first
            for i in range(len(first)):
                if second == first[:i] + first[i + 1:]:
                    return True
            return False

def main():
    print(Solution().oneEditAway("teacher", "treacher"))

if __name__ == "__main__":
    main()
