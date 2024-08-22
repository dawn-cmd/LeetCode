#include <bits/stdc++.h>
#define LL long long
#define mp(a, b) make_pair(a, b)
using namespace std;
class Solution
{
  public:
    int trap(vector<int> &height)
    {
        int maxe = distance(height.begin(), max_element(height.begin(), height.end()));
        int ans = 0;
        int max_lv = -1;
        for (int i = 0; i < maxe; ++i)
        {
            max_lv = max(height[i], max_lv);
            ans += max_lv - height[i];
        }
        max_lv = -1;
        for (int i = height.size() - 1; i > maxe; --i)
        {
            max_lv = max(height[i], max_lv);
            ans += max_lv - height[i];
        }
        return ans;
    }
};
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cout << setprecision(20);
}
