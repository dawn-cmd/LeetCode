#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        sort(seats.begin(), seats.end());
        sort(students.begin(), students.end());
        int ans = 0;
        for (int i = 0; i < seats.size(); ++i)
            ans += abs(seats[i] - students[i]);
        return ans;
    }
};

int main() { Solution sol; vector seats = {1, 2, 3}; vector students = {3, 2, 1}; int ans = sol.minMovesToSeat(seats, students); cout << "Expected output: 6" << endl; cout << "Actual output: " << ans << endl; return 0; }
