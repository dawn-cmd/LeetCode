//
// Created by LightString on 1/19/2023.
//
#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    static vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        unordered_map<int, unordered_set<int>> h;
        for (const auto &item: logs)
            h[item[0]].emplace(item[1]);
        vector<int> ans(k);
        for (const auto &item: h)
            ans[item.second.size() - 1]++;
        return ans;
    }
};
int main() {

}