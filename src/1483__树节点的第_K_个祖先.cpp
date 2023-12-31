#include <bits/stdc++.h>
using namespace std;
class TreeAncestor {
public:
    vector<vector<int>> dp;
    map<pair<int, int>, int> h;
    TreeAncestor(int n, vector<int>& parent) {
        for (int i = 0; i < n; ++i) {
            dp.emplace_back(vector<int>());
            dp[i].emplace_back(parent[i]);
        }
        for (int j = 1; ; ++j) {
            bool allneg = true;
            for (int i = 0; i < n; ++i) {
                dp[i].emplace_back(dp[i][j - 1] == -1 ? -1 : dp[dp[i][j - 1]][j - 1]);
                if (dp[i][j] != -1) allneg = false;
            }
            if (allneg) break;
        }
    }
    
    int getKthAncestor(int node, int k) {
        if (k == 0 || node == -1) return node;
        int pos = 0;
        int tmpk = k;
        while (!(tmpk & 1)) {
            tmpk >>= 1;
            pos++;
        }
        return pos < dp[node].size() ? getKthAncestor(dp[node][pos], k - (1 << pos)) : -1;
    }
};
int main() {
    
}
