#include "bits/stdc++.h"

using namespace std;

/**
 Definition for singly-linked list.
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr)
            return head;
        if (k <= 1)
            return head;
        ListNode* cur = head;
        vector<ListNode*> stk;
        stk.push_back(head);
        for (int i = 0; i < k - 1; ++i)
        {
            if (cur->next == nullptr)
                return head;
            cur = cur->next;
            stk.push_back(cur);
        }
        ListNode* nxt = stk[stk.size() - 1]->next;
        for (int i = stk.size() - 1; i > 0; --i)
            stk[i]->next = stk[i - 1];
        stk[0]->next = reverseKGroup(nxt, k);
        return stk[stk.size() - 1];
    }
};

int main()
{
    ListNode a(9);
    ListNode b(8, &a);
    ListNode c(7, &b);
    ListNode d(6, &c);
    ListNode e(5, &d);
    ListNode* head = Solution().reverseKGroup(&e, 2);
    while (head != nullptr)
    {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}
