struct Solution;
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut k = k;
        let mut bucket = vec![0; 20010];
        nums.iter().for_each(|x| {
            let id = *x + 10000;
            let id = id as usize;
            bucket[id] += 1;
        });
        let mut ans = 0;
        for num in (0..bucket.len()).rev() {
            ans = num as i32 - 10000;
            if k <= bucket[num] {
                break;
            }
            k -= bucket[num];
        }
        ans
    }
}
fn main() {
}
