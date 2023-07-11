#include <bits/stdc++.h>
using namespace std;
#define mp(x, y) make_pair(x, y)
class Solution {
private:
    vector<vector<int>> g;
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
    int dijkstra(int st, int ed, int n) {
        vector<int> dis(n, 0x3f3f3f3f);
        dis[st] = 0;
        priority_queue<pair<int, int>> q;
        q.push(mp(0, st));
        while (!q.empty()) {
            int cur = q.top().second;
            int d = q.top().first;
            q.pop();
            for (auto nxt: g[cur]) {
                if (dis[nxt] <= dis[cur] + 1) continue;
                dis[nxt] = dis[cur] + 1;
                q.push(mp(dis[nxt], nxt));
            }
        }
        return dis[ed] == 0x3f3f3f3f ? 0 : dis[ed] + 1;
    }

public:
    int ladderLength(string beginWord, string endWord, vector<string> &wordList) {
        int ed = -1;
        for (int i = 0; i < wordList.size(); ++i) {
            if (endWord == wordList[i]) {
                ed = i;
                break;
            }
        }
        if (ed == -1) return 0;
        init(beginWord, endWord, wordList);
        int st = wordList.size();
        return dijkstra(st, ed, wordList.size() + 1);
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<string> wordList{"hot", "dot", "dog", "lot", "log", "cog"};
    cout << Solution().ladderLength("hit", "cog", wordList) << '\n';
}
