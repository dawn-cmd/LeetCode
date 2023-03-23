//
// Created by LightString on 1/11/2023.
//
#include "bits/stdc++.h"
using namespace std;

class Solution
{
public:
    bool digitCount(string num)
    {
        unordered_map<char, int> h;
        for (const auto &c: num)
            h[c]++;
        for (int i = 0; i < num.size(); ++i)
            if (num[i] - '0' != h[('0' + i)])
                return false;
        return true;
    }
};

int main()
{
    cout << Solution().digitCount("030") << endl;
}