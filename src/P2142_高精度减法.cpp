#include <bits/stdc++.h>
#define LL long long
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    string a;
    string b;
    cin >> a >> b;
    bool neg_ans = 0;
    auto large_than = [](const string &a, const string &b) -> bool {
        if (a.size() > b.size()) return true;
        if (a.size() < b.size()) return false;
        return a > b;
    };
    if (large_than(b, a)) {
        swap(a, b);
        neg_ans = 1;
    }
    auto process = [](const string &s) -> vector<int> {
        vector<int> res;
        for (const auto &c: s) res.emplace_back(c - '0');
        reverse(res.begin(), res.end());
        return res;
    };
    vector<int> na = process(a);
    vector<int> nb = process(b);
    while (nb.size() < na.size()) nb.emplace_back(0);
    for (int i = 0; i < nb.size(); ++i) {
        if (na[i] < nb[i]) {
            na[i + 1] -= 1;
            na[i] += 10;
        }
        na[i] -= nb[i];
    }
    auto anti_process = [](vector<int> t) -> string {
        string res = "";
        for (const auto &num: t) res += '0' + num;
        reverse(res.begin(), res.end());
        int id = 0;
        while (id < res.size() - 1 && res[id] == '0') id++;
        res.erase(0, id);
        return res;
    };
    if (neg_ans) cout << '-';
    cout << anti_process(na) << '\n';
}
