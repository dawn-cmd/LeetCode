#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findMin(vector<int> &nums) {
        int low = 0;
        int high = nums.size() - 1;
        while (low < high) {
            int pivot = (low + high) >> 1;
            if (nums[pivot] < nums[high]) high = pivot;
            else if (nums[pivot] > nums[high])
                low = pivot + 1;
            else
                high -= 1;
        }
        return nums[low];
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> tmp{2, 2, 2, 0, 1};
    cout << Solution().findMin(tmp) << '\n';
}
