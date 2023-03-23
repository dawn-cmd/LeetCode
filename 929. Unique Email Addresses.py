from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for id in range(len(emails)):
            local = ""
            domain = ""
            for i in range(len(emails[id])):
                if emails[id][i] == '@':
                    local = emails[id][:i]
                    domain = emails[id][i + 1:]
                    break
            local = local.replace('.', '')
            for i in range(len(local)):
                if local[i] == '+':
                    local = local[:i]
                    break
            emails[id] = local + '@' + domain
        ans = set(emails)
        return len(ans)

def main():
    print(Solution().numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

if __name__ == "__main__":
    main()
