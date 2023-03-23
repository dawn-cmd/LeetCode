//
// Created by LightString on 1/11/2023.
//
#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge)
    {
        unordered_map<string, string> h;
        for (const auto &item: knowledge)
            h[item[0]] = item[1];
        int i = 0;
        string ans;
        while (i < s.size())
        {
            if (s[i] != '(')
            {
                ans += s[i];
                ++i;
                continue;
            }
            int j = i;
            while (s[j] != ')')
                ++j;
            string tmp = s.substr(i + 1, j - 1 - i - 1 + 1);
            if (h.count(tmp))
                ans.append(h[tmp]);
            else
                ans += '?';
            i = j + 1;
        }
        return ans;
    }
};

int main()
{

}