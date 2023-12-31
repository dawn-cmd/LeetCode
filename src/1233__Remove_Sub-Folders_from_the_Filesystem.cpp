#include "bits/stdc++.h"
using namespace std;

// Class definition for Solution
class Solution {
public:
    // Function to remove subfolders in a given vector of folders
    vector<string> removeSubfolders(vector<string> &folder) {
        // Sort the folder names in lexicographical order
        sort(folder.begin(), folder.end());

        // Use unordered_set to store unique folders
        unordered_set<string> uniqueFolders;

        // Loop through each folder name
        for (const auto &name: folder) {
            string parent = "";
            // Check if the current folder is a subfolder of an existing folder
            for (const auto &c: name) {
                if (c == '/' && uniqueFolders.count(parent)) {
                    // If the current folder is a subfolder, skip it
                    goto SKIP_FOLDER;
                }
                parent += c;
            }
            // If the folder is not a subfolder, add it to the unordered_set
            uniqueFolders.emplace(name);
            SKIP_FOLDER:;
        }
        // Convert the unordered_set to a vector and return it as the result
        return vector<string>(uniqueFolders.begin(), uniqueFolders.end());
    }
};

int main() {
    // Code outside of the Solution class is not given in the question
}
