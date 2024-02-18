/*
 * @lc app=leetcode.cn id=730 lang=rust
 *
 * [730] 统计不同回文子序列
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn count_palindromic_subsequences(s: String) -> i32 {
        let s = s.as_bytes();
        let MOD = 1e9 as i64 + 7;
        let mut dp = vec![vec![0; s.len() + 1]; s.len() + 1];
        for i in 0..=s.len() {
            dp[i][i] = 1;
        }
        for l in 2..=s.len() {
            for st in 0..=s.len() - l {
                let ed = st + l - 1;
                if s[st] != s[ed] {
                    dp[st][ed] = (dp[st + 1][ed] + dp[st][ed - 1] - dp[st + 1][ed - 1] + MOD) % MOD;
                    continue;
                }
                let mut x = st + 1;
                let mut y = ed - 1;
                while x <= y && s[st] != s[x] {
                    x += 1;
                }
                while x <= y && s[ed] != s[y] {
                    y -= 1;
                }
                dp[st][ed] = dp[st + 1][ed - 1] * 2 % MOD;
                if x > y {
                    dp[st][ed] = (dp[st][ed] + 2) % MOD;
                    continue;
                }
                if x == y {
                    dp[st][ed] = (dp[st][ed] + 1) % MOD;
                    continue;
                }
                dp[st][ed] = (dp[st][ed] + MOD - dp[x + 1][y - 1]) % MOD;
            }
        }
        (dp[0][s.len() - 1] % MOD) as i32
    }
}
// @lc code=end

fn main() {
    println!("{}", 938121524 % (1e9 as i32+7));
}
