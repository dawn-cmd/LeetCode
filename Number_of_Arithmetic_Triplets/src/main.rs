use std::collections::HashMap;
struct Solution;
impl Solution {
    pub fn arithmetic_triplets(nums: Vec<i32>, diff: i32) -> i32 {
        let mut hash = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            hash.entry(num).or_insert(1);
        }
        let mut ans = 0;
        for (i, num) in nums.iter().enumerate() {
            if hash.contains_key(&(num + diff)) && hash.contains_key(&(num + diff * 2)) {
                ans += 1;
            }
        }
        ans
    }
}
fn main() {
    println!("{}", Solution::arithmetic_triplets(vec![0, 1, 4, 6, 7, 10], 3));
}
