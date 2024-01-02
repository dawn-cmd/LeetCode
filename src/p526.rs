/*
 * @lc app=leetcode.cn id=526 lang=rust
 *
 * [526] 优美的排列
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn arrange_requirement(a: i32, b: i32) -> bool {
        a % b == 0 || b % a == 0
    }
    pub fn dfs_arrangement(n: i32, visited: &mut Vec<bool>, pos: i32) -> i32 {
        if pos > n {
            return 1;
        }
        let mut count = 0;
        for i in 1..=n {
            if !visited[i as usize] && Self::arrange_requirement(i, pos) {
                visited[i as usize] = true;
                count += Self::dfs_arrangement(n, visited, pos + 1);
                visited[i as usize] = false;
            }
        }
        count
    }
    pub fn count_arrangement(n: i32) -> i32 {
        let mut visited = vec![false; n as usize + 1];
        Self::dfs_arrangement(n, &mut visited, 1)
    }
}
// @lc code=end

