#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    string decodeMessage(string key, string message) {
        unordered_map<char, char> h;
        int cnt = 0;
        for (const auto &c: key) {
            if (c == ' ') continue;
            if (h.find(c) == h.end()) {
                h[c] = (char) ('a' + (cnt++));
                if (cnt == 26) break;
            }
        }
        string ans;
        for (const auto &c: message) {
            if (c == ' ') {
                ans.append(" ");
                continue;
            }
            ans += h[c];
        }
        return ans;
    }
};
int main() {
    cout << Solution().decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb") << '\n';
}
