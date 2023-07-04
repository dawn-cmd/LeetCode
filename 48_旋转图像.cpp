#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int tmp;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < i; ++j) {
                tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n/2; ++j) {
                tmp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = tmp;
            }
    }
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
}

