struct Solution {}
impl Solution {
    // The dfs function is a recursive function that performs depth-first search to find all
    // possible numbers with distinct digits within the given range.
    // cur: a mutable reference to the current number being evaluated.
    // used_digits: a mutable reference to a vector of flags indicating whether a digit has been used.
    // n: the upper limit of the range being evaluated.
    pub fn dfs(cur: &mut i64, used_digits: &mut Vec<bool>, n: i64) -> i64 {
        // If the current number is greater than the upper limit, return 0.
        if *cur > n {
            return 0;
        }
        // Initialize ans to 1, as the current number is counted as a number with distinct digits.
        let mut ans = 1;
        // Iterate through all possible digits.
        for digit in 0..10 {
            // If the current digit is 0 but the current number is 0, skip this iteration.
            if digit == 0 && *cur == 0 {
                continue;
            }
            // If the current digit has already been used, skip this iteration.
            if used_digits[digit] {
                continue;
            }
            // Flag the current digit as used.
            used_digits[digit] = true;
            // Add the current digit to the end of the current number.
            *cur = *cur * 10 + digit as i64;
            // Recursively call dfs with the updated current number and return value.
            ans += Self::dfs(cur, used_digits, n);
            // Unflag the current digit and remove it from the end of the current number.
            used_digits[digit] = false;
            *cur = *cur / 10;
        }
        // Return the total count of numbers with distinct digits within the given range.
        ans
    }
    // num_dup_digits_at_most_n is a function that calculates the number of distinct numbers
    // with duplicate digits at most n.
    // n: the upper limit of the range being evaluated.
    pub fn num_dup_digits_at_most_n(n: i32) -> i32 {
        // Convert n to an i64.
        let n = n as i64;
        // Initialize a vector of flags indicating whether a digit has been used.
        let mut used_digits = vec![false; 10];
        // Return the total count of distinct numbers with duplicate digits at most n.
        (n + 1 - Self::dfs(&mut 0, &mut used_digits, n)) as i32
    }
}
fn main() {
    // Call num_dup_digits_at_most_n with an upper limit of 1 billion (1,000,000,000).
    println!("{}", Solution::num_dup_digits_at_most_n(1000000000));
}
