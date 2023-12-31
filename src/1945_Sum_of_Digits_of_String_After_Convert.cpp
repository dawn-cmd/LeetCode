#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    int getLucky(string s, int k) {
        string ans = "";
        for (int i = 0; i < s.size(); ++i)
            ans += to_string((s[i] - 'a') + 1);
        while (k--)
        {
            long long tmp = 0;
            for (int i = 0; i < ans.size(); ++i)
                tmp += (ans[i] - '0');
            ans = to_string(tmp);
        }
        return stoi(ans);
    }
};

int main()
{
    string s;
    int k;
    cin >> s >> k;
    cout << Solution().getLucky(s, k) << endl;
}