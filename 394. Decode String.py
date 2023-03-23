class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        cnt = 0
        id = 0
        n = len(s)
        while id < n:
            if '0' <= s[id] <= '9':
                st = id
                while '0' <= s[id] <= '9' and id < n:
                    id += 1
                ed = id
                cnt = int(s[st:ed])
                continue
            if s[id] == '[':
                st = id
                layer = 1
                while layer > 0 and id < n:
                    id += 1
                    if s[id] == '[':
                        layer += 1
                    elif s[id] == ']':
                        layer -= 1
                ed = id
                for i in range(cnt):
                    ans += self.decodeString(s[st + 1:ed])
                id += 1
                continue
            ans += s[id]
            id += 1
        return ans

print(Solution().decodeString("2[abc]3[cd]ef"))
