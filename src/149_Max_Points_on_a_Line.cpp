// Include all standard library headers
#include <bits/stdc++.h>
using namespace std;

// Define a class called Solution
class Solution {
private:
    // Define a private method to compute the greatest common divisor
    int gcd(int a, int b) {
        if (a < b) swap(a, b);                        // Ensure that 'a' is not less than 'b'
        return b == 0 ? a : gcd(b, min(a % b, a - b));// Recursive Euclidean algorithm
    }

public:
    // Define a public method to find the maximum number of collinear points
    int maxPoints(vector<vector<int>> &points) {
        if (points.size() <= 2) return points.size();// If points size is 2 or less, return size as result
        int ans = -1;                                // Initialize the maximum number of collinear points
        unordered_map<int, int> h;                   // Map to store the count of points with the same slope

        // Iterate through all points
        for (int i = 0; i < points.size(); ++i) {
            h.clear();// Clear the map for every point
            for (int j = 0; j < points.size(); ++j) {
                if (j == i) continue;                // Skip if points are the same
                int dx = points[i][0] - points[j][0];// Compute difference in x-coordinates
                int dy = points[i][1] - points[j][1];// Compute difference in y-coordinates

                // Handle negative and zero differences
                if (dx < 0) dx *= -1, dy *= -1;
                if (dx == 0) dy = 1;
                else if (dy == 0)
                    dx = 1;
                else {
                    int tmp = gcd(abs(dx), abs(dy));// Compute gcd of differences
                    dx /= tmp, dy /= tmp;           // Simplify differences
                }

                h[dx * 100000 + dy]++;              // Increment the count of this slope
                ans = max(ans, h[dx * 100000 + dy]);// Update the maximum count if necessary
            }
        }
        return ans + 1;// Add 1 to the maximum count because the count starts from 0
    }
};

// The main function
int main() {
    ios::sync_with_stdio(0);// Untie stdio streams for performance
    cin.tie(0);             // Untie cin and cout streams for performance
}
