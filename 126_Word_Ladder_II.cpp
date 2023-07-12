#include <bits/stdc++.h>
using namespace std;
#define mp(x, y) make_pair(x, y)
class Solution {
private:
    vector<vector<int>> g;
    int minPath = 0x3f3f3f3f;
    vector<vector<int>> ans;
    int diffCount(const string &a, const string &b) {
        int cnt = 0;
        for (int i = 0; i < a.size(); ++i) cnt += a[i] != b[i];
        return cnt;
    }
    void init(const string &beginWord, const string &endWord, const vector<string> &wordList) {
        int st = wordList.size();
        g = vector<vector<int>>(wordList.size() + 1, vector<int>());
        for (int i = 0; i < wordList.size(); ++i) {
            if (diffCount(beginWord, wordList[i]) == 1) {
                g[st].emplace_back(i);
                g[i].emplace_back(st);
            }
        }
        for (int i = 0; i < wordList.size(); ++i) {
            for (int j = i + 1; j < wordList.size(); ++j) {
                if (diffCount(wordList[i], wordList[j]) != 1) continue;
                g[i].emplace_back(j);
                g[j].emplace_back(i);
            }
        }
    }
    void dfs(int cur, vector<int> &path, set<int> &vis, int ed) {
        if (cur == ed) {
            if (path.size() > minPath) return;
            if (minPath > path.size()) {
                ans.clear();
            }
            minPath = path.size();
            ans.emplace_back(path);
            return;
        }
        if (path.size() > minPath) return;
        for (auto nxt: g[cur]) {
            if (vis.find(nxt) != vis.end()) continue;
            path.emplace_back(nxt);
            vis.insert(nxt);
            dfs(nxt, path, vis, ed);
            path.pop_back();
            vis.erase(nxt);
        }
    }

public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string> &wordList) {
        int ed = -1;
        for (int i = 0; i < wordList.size(); ++i) {
            if (endWord == wordList[i]) {
                ed = i;
                break;
            }
        }
        if (ed == -1) return {};
        init(beginWord, endWord, wordList);
        for (int i = 0; i < g.size(); ++i) {
            cout << i << " -> ";
            for (auto j: g[i]) {
                cout << j << ' ';
            }
            cout << '\n';
        }
        vector<int> path{(int) wordList.size()};
        set<int> vis{(int) wordList.size()};
        dfs(wordList.size(), path, vis, ed);
        vector<vector<string>> tmp(ans.size());
        for (int i = 0; i < ans.size(); ++i) {
            for (auto j: ans[i]) {
                tmp[i].emplace_back(j == wordList.size() ? beginWord : wordList[j]);
            }
        }
        return tmp;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<string> wordList{"si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"};
    auto ans = Solution().findLadders("qa", "sq", wordList);
    for (int i = 0; i < ans.size(); ++i) {
        for (auto j: ans[i]) {
            cout << j << ' ';
        }
        cout << '\n';
    }
}
