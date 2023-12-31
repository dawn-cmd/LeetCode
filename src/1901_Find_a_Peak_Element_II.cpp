/********************************************************************************
* @author: Huaiyuan Jing
* @email: ls.hyjing@gmail.com
* @version: 1.0
* @description:
********************************************************************************/
#include <bits/stdc++.h>
#define LL long long
#define mp(a, b) make_pair(a, b)
using namespace std;
class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {
        mat.insert(mat.begin(), vector<int>(mat[0].size(), -1));
        mat.emplace_back(vector<int>(mat[0].size(), -1));
        int n = mat.size() - 2;
        for (int i = 0; i < mat.size(); ++i) {
            mat[i].insert(mat[i].begin(), -1);
            mat[i].emplace_back(-1);
        }

        // Test Preprocess of Graph
        // for (auto row : mat) {
        //     for (auto element : row) {
        //         cout << element << ' ';
        //     }
        //     cout << '\n';
        // }

        int st = 1;
        int ed = mat.size() - 2;
        while (true) {
            int mid = (st + ed) >> 1;
            int maxn = distance(mat[mid].begin(),
                max_element(mat[mid].begin(), mat[mid].end()));
            if (mid + 1 <= ed && mat[mid][maxn] < mat[mid + 1][maxn]) {
                st = mid + 1;
                continue;
            }
            if (mid - 1 >= st && mat[mid][maxn] < mat[mid - 1][maxn]) {
                ed = mid - 1;
                continue;
            }
            return { mid - 1, maxn - 1 };
        }
        return { 0 };
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cout << setprecision(20);

}
