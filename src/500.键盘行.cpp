/*
 * @lc app=leetcode.cn id=500 lang=cpp
 *
 * [500] 键盘行
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
    vector<string> findWords(vector<string> &words)
    {
        string lines[3] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        map<char, int> h;
        for (int i = 0; i < 3; i++)
        {
            for (auto &c : lines[i])
            {
                h[c] = i;
                h[toupper(c)] = i;
            }
        }
        vector<string> ans;
        for (auto &word : words)
        {
            int tmp = h[word[0]];
            bool isSameLine = true;
            for (int i = 1; i < word.size() && isSameLine; i++)
            {
                if (h[word[i]] != tmp)
                    isSameLine = false;
            }
            if (isSameLine)
                ans.push_back(word);
        }
        return ans;
    }
};
// @lc code=end
