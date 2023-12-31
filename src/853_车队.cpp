#include <bits/stdc++.h>
#define LL long long
#define mp(a, b) make_pair(a, b)
using namespace std;
class Solution {
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed) {
        int n = position.size();
        vector<pair<int, int>> cars(n);
        for (int i = 0; i < n; ++i) cars[i] = mp(position[i], speed[i]);
        sort(cars.begin(), cars.end());
        double previous_time = 0;
        int res = 0;
        for (int i = n - 1; i >= 0; --i) {
            if ((double) (target - cars[i].first) / (double) (cars[i].second) > previous_time) {
                previous_time = (double) (target - cars[i].first) / (double) (cars[i].second);
                ++res;
            }
        }
        return res;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
}
