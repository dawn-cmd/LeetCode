use std::collections::HashMap;
struct Solution {}
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        let mut id = 0x3f3f3f3f;
        for i in 0..nums.len() {
            if nums[i] == k {
                id = i;
                nums[i] = 0;
                continue;
            }
            nums[i] = if nums[i] > k { 1 } else { -1 };
        }
        // println!("{:?}", nums);
        let mut h = HashMap::new();
        let mut prefix = vec![0; nums.len()];
        let mut ans = 0;
        h.insert(0, 1);
        for i in 0..nums.len() {
            prefix[i] = if i == 0 {
                nums[0]
            } else {
                prefix[i - 1] + nums[i]
            };
            if i < id {
                h.entry(prefix[i])
                    .and_modify(|value| *value += 1)
                    .or_insert(1);
                continue;
            }
            if let Some(value) = h.get(&prefix[i]) {
                ans += *value;
            }
            if let Some(value) = h.get(&(prefix[i] - 1)) {
                ans += *value;
            }
        }
        return ans;
    }
}
fn main() {
    println!("{}", Solution::count_subarrays(vec![3, 2, 1, 4, 5], 4));
}
