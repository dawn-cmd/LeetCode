#include "bits/stdc++.h"
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode head(0, list1);
        ListNode *tmp1;
        ListNode *cur = &head;
        while (a--) cur = cur->next;
        tmp1 = cur;
        ListNode *tmp2;
        cur = &head;
        while (b--) cur = cur->next;
        tmp2 = cur->next->next;
        tmp1->next = list2;
        cur = list2;
        while (cur->next != nullptr) cur = cur->next;
        cur->next = tmp2;
        return head.next;
    }
};
