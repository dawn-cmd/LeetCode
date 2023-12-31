#include <bits/stdc++.h>
using namespace std;

class Solution 
{
public:
    int minimumMoves(string s) 
    {
        vector<int> dp(s.size());
        for (int i = 0; i < 3; ++i)
        {
            if (i > 0 && dp[i - 1] == 1)
            {
                dp[i] = 1;
                continue;
            }
            dp[i] = s[i] == 'X' ? 1 : 0;
        }
        for (int i = 3; i < s.size(); ++i)
        {
            if (s[i] == 'O')
            {
                dp[i] = dp[i - 1];
                continue;
            }
            dp[i] = dp[i - 3] + 1;
        }
        return dp[s.size() - 1];
    }
};

int main()
{
    cout << Solution().minimumMoves("XXOX") << endl;
}
