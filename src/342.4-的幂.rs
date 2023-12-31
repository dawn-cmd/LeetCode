/*
 * @lc app=leetcode.cn id=342 lang=rust
 *
 * [342] 4的幂
 */

// @lc code=start
impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        return (n > 0) && (n as u32 & 0xaaaaaaaa) == 0 && (n & -n == n);
    }
}
// @lc code=end
