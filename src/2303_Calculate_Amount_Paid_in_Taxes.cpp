//
// Created by LightString on 1/22/2023.
//
#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    static double calculateTax(vector<vector<int>>& brackets, int income) {
        double ans = 0;
        for (int i = 0; i < brackets.size(); ++i)
        {
            if (income >= brackets[i][0])
            {
                ans += (double)((i == 0 ? brackets[i][0] : brackets[i][0] - brackets[i - 1][0]) * brackets[i][1]) / 100;
                continue;
            }
            ans += (double)((i == 0 ? income : income - brackets[i - 1][0]) * brackets[i][1]) / 100;
            break;
        }
        return ans;
    }
};
int main() {

}