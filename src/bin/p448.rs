/*
 * @lc app=leetcode.cn id=448 lang=rust
 *
 * [448] 找到所有数组中消失的数字
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut nums: Vec<usize> = nums.iter().map(|x| *x as usize).collect();
        for i in 0..nums.len() {
            while nums[i] != i + 1 && nums[i] != nums[nums[i] - 1] {
                let temp = nums[i];
                nums[i] = nums[temp as usize - 1];
                nums[temp as usize - 1] = temp;
            }
        }
        nums.iter()
            .enumerate()
            .filter(|(i, &x)| *i != x as usize - 1)
            .map(|(i, _)| i as i32 + 1)
            .collect()
    }
}
// @lc code=end
fn main() {
    // Test cases
    let test_cases = vec![
        (vec![4, 3, 2, 7, 8, 2, 3, 1], vec![5, 6]),
        (vec![1, 1], vec![2]),
        (vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], vec![]),
    ];

    for (nums, expected) in test_cases {
        let result = Solution::find_disappeared_numbers(nums);
        assert_eq!(result, expected);
    }
}
