#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<string> fullJustify(vector<string> &words, int maxWidth) {
        vector<string> ans;
        int id = 0;
        while (id < words.size()) {
            int remain = maxWidth - words[id].size();
            int cnt = 1;
            string txt = "";
            while (id + cnt < words.size() && remain >= words[id + cnt].size() + 1) {
                remain -= words[id + cnt].size() + 1;
                cnt++;
            }
            txt += words[id];
            if (cnt == 1) {
                while (txt.size() < maxWidth) txt += ' ';
                ans.emplace_back(txt);
                id += cnt;
                continue;
            }
            if (id + cnt == words.size()) {
                for (int i = id + 1; i < id + cnt; ++i) txt += ' ' + words[i];
                while (txt.size() < maxWidth) txt += ' ';
                ans.emplace_back(txt);
                id += cnt;
                continue;
            }
            int avg_space = remain / (cnt - 1);
            int left_add = remain % (cnt - 1);
            for (int i = id + 1; i < id + cnt; ++i) {
                for (int j = 0; j < avg_space + 1 + (i - id <= left_add ? 1 : 0); ++j) txt += ' ';
                txt += words[i];
            }
            ans.emplace_back(txt);
            id += cnt;
        }
        return ans;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<string> tmp{"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"};
    vector<string> ans = Solution().fullJustify(tmp, 20);
    for (const auto &s: ans) cout << s << '\n';
}
