#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int candy(vector<int> &ratings) {
        vector<int> candies(ratings.size(), 1);
        for (int i = 1; i < ratings.size(); ++i) {
            if (ratings[i] <= ratings[i - 1]) continue;
            candies[i] = candies[i - 1] + 1;
        }
        for (int i = ratings.size() - 2; i >= 0; --i) {
            if (ratings[i] <= ratings[i + 1]) continue;
            candies[i] = max(candies[i], candies[i + 1] + 1);
        }
        int ans = 0;
        for (auto candy: candies) ans += candy;
        return ans;
    
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
}
