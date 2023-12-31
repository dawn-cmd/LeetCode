#include <bits/stdc++.h>
#define LL long long
#define cout cout<<setprecision(20)
#define mp(a, b) make_pair(a, b)
using namespace std;
class Solution {
public:
    int splitNum(int num) {
        register vector<int> nums;
        while (num) {
            nums.emplace_back(num % 10);
            num /= 10;
        }
        sort(nums.begin(), nums.end());
        int num1 = 0;
        for (int i = 0; i < nums.size(); i += 2) {
            num1 = num1 * 10 + nums[i];
        }
        int num2 = 0;
        for (int i = 1; i < nums.size(); i += 2) {
            num2 = num2 * 10 + nums[i];
        }
        return num1 + num2;
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

}
