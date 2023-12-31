#include <bits/stdc++.h>
#define MOD (long long)(1e9 + 7)
using namespace std;

class Solution {
public:
    int countHomogenous(string s) {
        s += '#';
        long long cnt = 1;
        long long ans = 0;
        for (int i = 1; i < s.size(); ++i)
            if (s[i] != s[i - 1])
            {
                ans = (ans + cnt * (cnt + 1) / 2) % MOD;
                cnt = 1;
            }
            else
                cnt += 1;
        return ans;
    }
};

int main()
{
    cout << Solution().countHomogenous("abbcccaa") << endl;
}
