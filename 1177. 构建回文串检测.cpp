#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> h;
    bool test(const string &s, int left, int right, int k) {
        int cntOgg = 0;
        for (int i = 0; i < 26; ++i) {
            if ((h[right][i] - (left == 0 ? 0 : h[left - 1][i])) & 1) {
                cntOgg++;
            }
        }
        return cntOgg / 2 <= k;
    }
    vector<bool> canMakePaliQueries(string s, vector<vector<int>> &queries) {
        h.resize(s.size());
        for (int i = 0; i < h.size(); ++i) {
            h[i] = vector<int>(26);
        }
        for (int i = 0; i < h.size(); ++i) {
            for (int j = 0; j < 26; ++j) {
                h[i][j] = (i == 0) ? 0 : h[i - 1][j];
            }
            h[i][s[i] - 'a'] += 1;
        }
        vector<bool> ans;
        for (auto query: queries) {
            ans.emplace_back(test(s, query[0], query[1], query[2]));
        }
        return ans;
    }
};
int main() {
}
