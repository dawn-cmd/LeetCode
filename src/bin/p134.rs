/*
 * @lc app=leetcode.cn id=134 lang=rust
 *
 * [134] 加油站
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n = gas.len();
        let mut diff = vec![];
        for i in 0..n * 2 {
            diff.push(gas[i % n] - cost[i % n]);
        }
        let mut left_gas = 0;
        let mut min_gas = 0x3f3f3f3f;  // The least gas appeared in iteration
        let mut min_pos = 0;  // where is the min value
        for i in 0..n {
            left_gas += diff[i];
            if left_gas < min_gas {
                min_gas = left_gas;
                min_pos = i;
            }
        }
        if left_gas < 0 {
            -1
        } else {
            if min_gas >= 0 {
                0
            } else {
                (min_pos as i32 + 1) % n as i32
            }
        }
    }
}
// @lc code=end

fn main() {
    println!("{}", Solution::can_complete_circuit(vec![0, 0, 0, 3, 3], vec![2, 2, 2, 0, 0]));
}
