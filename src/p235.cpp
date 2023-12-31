/*
 * @lc app=leetcode.cn id=235 lang=cpp
 *
 * [235] 二叉搜索树的最近公共祖先
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
/**
 * Definition for a binary tree node.
 *
 */
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL)
    {
    }
};
// @lc code=start

class Solution
{
  public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        if (p->val > q->val)
            swap(p, q);
        set<int> visited;
        map<TreeNode *, TreeNode *> fa;
        auto tmp = root;
        while (tmp != nullptr && tmp != p)
        {
            visited.insert(tmp->val);
            if (tmp->val > p->val)
                tmp = tmp->left;
            else if (tmp->val < p->val)
                tmp = tmp->right;
        }
        visited.insert(p->val);
        tmp = root;
        auto previous = tmp;
        while (tmp != nullptr && tmp != q)
        {
            previous = tmp;
            if (tmp->val > q->val)
                tmp = tmp->left;
            else
                tmp = tmp->right;
            fa[tmp] = previous;
        }
        while (visited.find(q->val) == visited.end() && fa.find(q) != fa.end())
        {
            cout << q->val << '\n';
            q = fa[q];
        }
        return q;
    }
};
// @lc code=end
