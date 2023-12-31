//
// Created by LightString on 1/9/2023.
//
#include "bits/stdc++.h"
using namespace std;

class Solution
{
public:
    unordered_set<int> h;
    int highest = 0;

    void dfs(int node, string &ans, const int &k)
    {
        for (int i = 0; i < k; ++i)
            if (!h.count(node * 10 + i))
            {
                h.emplace(node * 10 + i);
                dfs((node * 10 + i) % highest, ans, k);
                ans += to_string(i);
            }
    }

    string crackSafe(int n, int k)
    {
        string ans;
        highest = (int)pow(10, n - 1);
        dfs(0, ans, k);
        ans += string(n - 1, '0');
        return ans;
    }
};

int main()
{
    printf("%s", Solution().crackSafe(2, 2).c_str());
}