//
// Created by LightString on 1/23/2023.
//
#include "bits/stdc++.h"
using namespace std;
class Solution {
private:
    static bool pointIsInRound(const vector<int> &point, const vector<int> &round) {
        return (round[2] * round[2]) >= ((point[0] - round[0]) * (point[0] - round[0]) + (point[1] - round[1]) * (point[1] - round[1]));
    }
public:
    static vector<int> countPoints(const vector<vector<int>>& points, const vector<vector<int>>& queries) {
        vector<int> ans(queries.size());
        int id = 0;
        for (const auto &query: queries)
        {
            for (const auto &point: points)
                ans[id] += pointIsInRound(point, query);
            ++id;
        }
        return ans;
    }
};
int main() {
    vector<vector<int>> points{{1, 3}, {3, 3}, {5, 3}, {2, 2}};
    vector<vector<int>> queries{{2, 3, 1}, {4, 3, 1}, {1, 1, 2}};
    vector<int> ans = Solution().countPoints(points, queries);
    for (const auto num: ans)
        cout << num << ' ';
    cout << '\n';
}