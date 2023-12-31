//
// Created by LightString on 1/7/2023.
//
#include "bits/stdc++.h"
using namespace std;

class Solution {
public:

    bool checkPrefix(const string &prefix, const string &word)
    {
        for (int i = 0; i < prefix.size(); ++i)
            if (prefix[i] != word[i])
                return false;
        return true;
    }

    int prefixCount(const vector<string>& words, const string &pref) {
        int ans = 0;
        for (const auto &word: words)
            if (checkPrefix(pref, word))
                ans++;
        return ans;
    }
};