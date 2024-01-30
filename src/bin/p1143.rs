/*
 * @lc app=leetcode.cn id=1143 lang=rust
 *
 * [1143] 最长公共子序列
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let text1: Vec<char> = text1.chars().collect();
        let text2: Vec<char> = text2.chars().collect();
        let n = text1.len();
        let m = text2.len();
        let mut dp = vec![vec![0; m + 1]; n + 1];
        for i in 1..=n {
            for j in 1..=m {
                // println!("i = {}, j = {}", i, j);
                dp[i][j] = if text1[i - 1] == text2[j - 1] {
                    dp[i - 1][j - 1] + 1
                } else {
                    dp[i - 1][j].max(dp[i][j - 1])
                };
            }
        }
        dp[n][m]
    }
}
// @lc code=end

fn main() {
    let text1 = String::from("abcde");
    let text2 = String::from("ace");
    let result = Solution::longest_common_subsequence(text1, text2);
    println!("Longest common subsequence length: {}", result);
}
