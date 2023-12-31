#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    string largestMerge(string word1, string word2) {
        string merge;
        int id1 = 0;
        int id2 = 0;
        int l1 = word1.size();
        int l2 = word2.size();
        while (id1 < l1 || id2 < l2)
            if (id1 < l1 && word1.substr(id1) > word2.substr(id2))
                merge.push_back(word1[id1++]);
            else
                merge.push_back(word2[id2++]);
        return merge;
    }
};

int main() {
    cout << Solution().largestMerge("cabaa", "bcaaa") << endl;
}
