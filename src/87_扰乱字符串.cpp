#include <bits/stdc++.h>
using namespace std;

class Solution
{
  public:
    bool isScramble(string s1, string s2)
    {
        if (s1.size() != s2.size())
            return false;

        int n = s1.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(n, 0)));

        return solve(s1, s2, 0, 0, n, dp);
    }

  private:
    bool solve(const string &s1, const string &s2, int i, int j, int len, vector<vector<vector<int>>> &dp)
    {
        if (len == 1)
            return s1[i] == s2[j];

        if (s1.substr(i, len) == s2.substr(j, len))
            return true;

        if (dp[i][j][len] != 0)
            return dp[i][j][len] == 1;

        for (int k = 1; k < len; ++k)
        {
            if ((solve(s1, s2, i, j, k, dp) && solve(s1, s2, i + k, j + k, len - k, dp)) ||
                (solve(s1, s2, i, j + len - k, k, dp) && solve(s1, s2, i + k, j, len - k, dp)))
            {
                dp[i][j][len] = 1;
                return true;
            }
        }

        dp[i][j][len] = -1;
        return false;
    }
};

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    // Example usage
    Solution solution;
    string s1 = "great", s2 = "rgeat";
    cout << (solution.isScramble(s1, s2) ? "True" : "False") << endl;

    return 0;
}
