struct Solution {}
impl Solution {
    pub fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort_unstable();
        let mut ans: Vec<Vec<i32>> = vec![];
        for k in 0..nums.len() {
            if nums[k] > target && nums[k] >= 0 {
                break;
            }
            if k > 0 && nums[k] == nums[k - 1] {
                continue;
            }
            for i in k + 1..nums.len() {
                if nums[i] + nums[k] > target && nums[i] + nums[k] >= 0 {
                    break;
                }
                if i > k + 1 && nums[i] == nums[i - 1] {
                    continue;
                }
                let mut left = i + 1;
                let mut right = nums.len() - 1;
                while right > left {
                    let sum: i64 =
                        nums[k] as i64 + nums[i] as i64 + nums[left] as i64 + nums[right] as i64;
                    if sum > target as i64 {
                        right -= 1;
                    } else if sum < target as i64 {
                        left += 1;
                    } else {
                        ans.push(vec![nums[k], nums[i], nums[left], nums[right]]);
                        while right > left && nums[left] == nums[left + 1] {
                            left += 1;
                        }
                        while right > left && nums[right] == nums[right - 1] {
                            right -= 1;
                        }
                        left += 1;
                        right -= 1;
                    }
                }
            }
        }
        return ans;
    }
}
fn main() {
    println!("{:?}", Solution::four_sum(vec![1, 0, -1, 0, -2, 2], 0));
}
