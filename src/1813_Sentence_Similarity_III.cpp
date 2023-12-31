//
// Created by LightString on 1/15/2023.
//
#include "bits/stdc++.h"
using namespace std;
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        if (sentence1 == sentence2)
            return true;
        if (sentence1.size() < sentence2.size())
            swap(sentence1, sentence2);
        long long n1 = sentence1.size() + 1;
        long long n2 = sentence2.size() + 1;
        sentence1 = ' ' + sentence1;
        sentence2 = ' ' + sentence2;
        int id1 = 0;
        int id2 = 0;
        while (sentence1[id1] == sentence2[id2] && id1 < n1 && id2 < n2)
        {
            id1++;
            id2++;
        }
        if (id2 == n2)
            if (sentence1[id1] == ' ')
                return true;
        while (sentence1[id1] != ' ' || sentence2[id2] != ' ')
        {
            id1--;
            id2--;
        }
        id1 = n1 - (n2 - id2);
        while (id1 < n1 && id2 < n2)
        {
            if (sentence1[id1] != sentence2[id2])
                return false;
            id1++;
            id2++;
        }
        return true;
    }
};

int main() {
    cout << Solution().areSentencesSimilar("L", "Lucccky") << endl;
}