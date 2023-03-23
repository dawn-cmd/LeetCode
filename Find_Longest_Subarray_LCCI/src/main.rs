use std::collections::HashMap;
struct Solution {}
impl Solution {
    pub fn find_longest_subarray(array: Vec<String>) -> Vec<String> {
        let mut prefix_count: HashMap<i32, i32> = HashMap::new();
        prefix_count.insert(0, -1);
        let mut ans: i32 = 0;
        let mut id: i32 = 0;
        let mut prefix: i32 = 0;
        for (i, s) in array.iter().enumerate() {
            let first_c = s.chars().nth(0);
            prefix += if Some('0') <= first_c && first_c <= Some('9') {
                1
            } else {
                -1
            };
            if !prefix_count.contains_key(&prefix) {
                prefix_count.insert(prefix, i as i32);
                continue;
            }
            let left = *prefix_count.get(&prefix).unwrap();
            if i as i32 - left + 1 > ans {
                ans = i as i32 - left + 1;
                id = left;
            }
        }
        return if id + 1 < id + ans {
            array[(id + 1) as usize..(id + ans) as usize].to_vec()
        } else {
            vec![]
        };
    }
}
fn main() {
    println!(
        "{:?}",
        Solution::find_longest_subarray(vec![String::from("A")])
    );
}
