#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if (s1.size() != s2.size()) return false;
        int dp[31][31][31];
        for (int len = 1; len <= s1.size(); ++len) {
            for (int i = 0; i + len - 1 < s1.size(); ++i) {
                for (int j = 0; j + len - 1 < s2.size(); ++j) {
                    if (len == 1) {
                        dp[i][j][len] = (s1[i] == s2[j]);
                        continue;
                    }
                    if (s1.substr(i, len) == s2.substr(j, len)) {
                        dp[i][j][len] = 1;
                        continue;
                    }
                    dp[i][j][len] = 0;
                    for (int k = 1; k < len && !dp[i][j][len]; ++k) {
                        dp[i][j][len] |= dp[i][j][k] & dp[i + k][j + k][len - k];
                        dp[i][j][len] |= dp[i][j + len - k][k] & dp[i + k][j][len - k];
                    }
                }
            }
        }
        return dp[0][0][s1.size()];
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
}
