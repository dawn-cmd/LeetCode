/*
 * @lc app=leetcode.cn id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */
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
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cout << setprecision(20);
}

// @lc code=start
class Solution
{
  public:
    double binaryPow(double x, long long n)
    {
        if (!n)
            return 1;
        /*Deal n as a binary number, each "1" means multiply with the power at that position. For example 5 to 0101, which means multiply x^5 = x^4 * x^1*/
        return ((n & 1) ? x : 1) * binaryPow(x * x, n >> 1);
    }
    double myPow(double x, int n)
    {
        if (x == 0)
            return 0;
        if (n == 0 || x == 1)
            return 1;
        if (n < 0)
            return 1 / binaryPow(x, -(long long)n);
        else
            return binaryPow(x, (long long)n);
    }
};
// @lc code=end
