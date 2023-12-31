/*
 * @lc app=leetcode.cn id=220 lang=rust
 *
 * [220] 存在重复元素 III
 */
struct Solution {}

// @lc code=start
use std::collections::BTreeMap;

/// Determines whether there exists a pair of elements in the given `nums` vector such that their absolute difference is at most `value_diff` and their indices differ by at most `index_diff`.
///
/// # Arguments
///
/// * `nums` - A vector of integers.
/// * `index_diff` - The maximum allowed difference between the indices of the pair of elements.
/// * `value_diff` - The maximum allowed absolute difference between the values of the pair of elements.
///
/// # Returns
///
/// Returns `true` if there exists a pair of elements satisfying the conditions, otherwise returns `false`.
///
/// # Examples
///
/// ```
/// let nums = vec![1, 2, 3, 1];
/// let index_diff = 3;
/// let value_diff = 0;
/// assert_eq!(Solution::contains_nearby_almost_duplicate(nums, index_diff, value_diff), true);
/// ```
impl Solution {
    pub fn contains_nearby_almost_duplicate(
        nums: Vec<i32>,
        index_diff: i32,
        value_diff: i32,
    ) -> bool {
        let mut sliding_window: BTreeMap<i32, i32> = BTreeMap::new();

        for i in 0..nums.len() {
            Self::remove_out_of_window(&mut sliding_window, &nums, i, index_diff);
            if Self::has_nearby_almost_duplicate(&sliding_window, nums[i], value_diff) {
                return true;
            }
            Self::add_to_sliding_window(&mut sliding_window, nums[i]);
        }

        false
    }

    // Removes elements from the sliding window that are out of the window range
    fn remove_out_of_window(
        sliding_window: &mut BTreeMap<i32, i32>,
        nums: &Vec<i32>,
        index: usize,
        index_diff: i32,
    ) {
        // There is still nothing needs to be removed
        if index <= index_diff as usize {
            return;
        }
        // minus the count by 1
        if let Some(value) = sliding_window.get_mut(&nums[index - index_diff as usize - 1]) {
            *value -= 1;
        }
        if sliding_window[&nums[index - index_diff as usize - 1]] == 0 {
            sliding_window.remove(&nums[index - index_diff as usize - 1]);
        }
    }

    // Checks if there exists a nearby almost duplicate element in the sliding window
    fn has_nearby_almost_duplicate(
        sliding_window: &BTreeMap<i32, i32>,
        num: i32,
        value_diff: i32,
    ) -> bool {
        sliding_window
            .range(num - value_diff..=num + value_diff)
            .next()
            .is_some()
    }

    // Adds an element to the sliding window
    fn add_to_sliding_window(sliding_window: &mut BTreeMap<i32, i32>, num: i32) {
        let entry = sliding_window.entry(num).or_insert(0);
        *entry += 1;
    }
}
// @lc code=end
