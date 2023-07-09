#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ans;
        int n = words[0].size();
        int m = words.size();
        int ls = s.size();
        for (int i = 0; i < n && i + n * m - 1 < ls; ++i) {
            unordered_map<string, int> h;
            for (int j = 0; j < m; ++j) {
                ++h[s.substr(i + j * n, n)];
            }
            for (auto word: words) {
                if (--h[word] == 0) {
                    h.erase(word);
                }
            }
            for (int left = i; left + n * m <= ls; left += n) {
                if (left == i) {
                    if (h.empty()) {
                        ans.emplace_back(left);
                    }
                    continue;
                }
                string word = s.substr(left + n * (m - 1), n);
                if (++h[word] == 0) {
                    h.erase(word);
                }
                word = s.substr(left - n, n);
                if (--h[word] == 0) {
                    h.erase(word);
                }
                if (h.empty()) {
                    ans.emplace_back(left);
                }
            } 
        }
        return ans;
    }
};
