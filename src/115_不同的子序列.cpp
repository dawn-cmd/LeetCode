#include <bits/stdc++.h>
#define ULL unsigned long long
using namespace std;
class Solution {
public:
    int numDistinct(const string &s, const string &t) {
        ULL dp[1010][1010];
        for (int j = 0; j < t.size(); ++j) {
            for (int i = 0; i < s.size(); ++i) {
                if (i < j) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i == j) {
                    dp[i][j] = s.substr(0, i + 1) == t.substr(0, j + 1) ? 1 : 0;
                    continue;
                }
                dp[i][j] = dp[i - 1][j];
                if (s[i] == t[j]) dp[i][j] += j == 0 ? 1 : dp[i - 1][j - 1];
            }
        }
        return dp[s.size() - 1][t.size() - 1];
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
}

