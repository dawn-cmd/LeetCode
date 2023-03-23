struct Solution {}
impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let mut pref = vec![nums[0]];
        for i in 1..(nums.len()) {
            pref[i] = pref[i - 1] + nums[i];
        }
        
    }
}
fn main() {
    println!("Hello, world!");
}
