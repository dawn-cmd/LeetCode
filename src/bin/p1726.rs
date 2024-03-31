use std::collections::HashMap;

/*
 * @lc app=leetcode.cn id=1726 lang=rust
 *
 * [1726] 同积元组
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let mut h = HashMap::new();
        let n = nums.len();
        for i in 0..n {
            for j in i + 1..n {
                *h.entry(nums[i] * nums[j]).or_insert(0) += 1;
            }
        }
        let mut ans = 0;
        for i in 0..n {
            for j in i + 1..n {
                ans += h.get(&(nums[i] * nums[j])).unwrap_or(&0) - 1;
            }
        }
        ans * 4
    }
}
// @lc code=end

fn main() {

}
