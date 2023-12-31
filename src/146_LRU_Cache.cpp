#include "bits/stdc++.h"
using namespace std;

class Node
{
public:
    int key;
    int val;
    Node* prev;
    Node* next;

    Node()
    {
        this->key = -1;
        this->val = -1;
    }
};

class LRUCache {
public:
    map<int, Node> h;
    Node* head;
    Node* end;
    int cap;
    int nums;
    LRUCache(int capacity) {
        head = new Node();
        end = new Node();
        head->next = end;
        end->prev = head;
        cap = capacity;
        nums = 0;
    }

    int get(int key) {
        if (!h.count(key))
            return -1;
        removeNode(&h[key]);
        addToHead(&h[key]);
        return h[key].val;
    }

    void put(int key, int value) {
        if (h.count(key))
        {
            h[key].val = value;
            removeNode(&h[key]);
            addToHead(&h[key]);
            return;
        }
        Node tmp;
        tmp.val = value;
        tmp.key = key;
        addToHead(&tmp);
        h[key] = tmp;
        nums += 1;
        if (nums > cap)
        {
            h.erase(end->prev->key);
            delete removeNode(end->prev);
            nums -= 1;
        }
    }

    Node* removeNode(Node* node)
    {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        return node;
    }

    void addToHead(Node* node)
    {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }
};

int main()
{
    LRUCache test(2);
    test.put(1, 1);
    test.put(2, 2);
    cout << test.get(1) << endl;
    test.put(3, 3);
    cout << test.get(2) << endl;
    test.put(4, 4);
    cout << test.get(1) << endl;
    cout << test.get(3) << endl;
    cout << test.get(4) << endl;
}