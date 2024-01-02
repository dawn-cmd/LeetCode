/*
 * @lc app=leetcode.cn id=466 lang=rust
 *
 * [466] 统计重复个数
 */

struct Solution;
// @lc code=start
use std::collections::HashMap;
use std::collections::HashSet;
impl Solution {
    pub fn get_max_repetitions(s1: String, n1: i32, s2: String, n2: i32) -> i32 {
        if !Solution::feasibility_judge(s1.clone(), s2.clone()) {
            return 0;
        }
        let s1 = Solution::to_vector_char(s1);
        let s2 = Solution::to_vector_char(s2);
        let mut s1_cnt = 0;
        let mut s2_cnt = 0;
        let mut p2: i32 = 0;
        let mut matched_map: HashMap<i32, (i32, i32)> = HashMap::new();
        while true {
            s1_cnt += 1;
            for i in 0..s1.len() {
                if !(s1[i as usize] == s2[p2 as usize]) {
                    continue;
                }
                (p2, s2_cnt) = Solution::update_id(p2, s2_cnt, s2.len() as i32);
            }
            if s1_cnt == n1 {
                return s2_cnt / n2;
            }
            if matched_map.contains_key(&p2) {
                break;
            }
            matched_map.insert(p2, (s1_cnt, s2_cnt));
        }
        let pre_loop = matched_map.get(&p2).unwrap();
        let in_loop = (s1_cnt - pre_loop.0, s2_cnt - pre_loop.1);
        let mut ans = pre_loop.1 + (n1 - pre_loop.0) / in_loop.0 * in_loop.1;
        let rest = (n1 - pre_loop.0) % in_loop.0;
        ans += Solution::calculate_leftover(s1, s2, p2, rest);
        ans / n2
    }
    pub fn calculate_leftover(s1: Vec<char>, s2: Vec<char>, p2: i32, rest: i32) -> i32 {
        let mut p2 = p2;
        let mut ans = 0;
        for _ in 0..rest {
            for ch in s1.clone() {
                if !(ch == s2[p2 as usize]) {
                    continue;
                }
                println!("p2: {}, ans: {}", p2, ans);
                (p2, ans) = Solution::update_id(p2 as i32, ans, s2.len() as i32);
            }
        }
        ans
    }
    pub fn to_vector_char(s: String) -> Vec<char> {
        let mut tmp = vec![];
        for ch in s.chars() {
            tmp.push(ch);
        }
        tmp
    }
    pub fn feasibility_judge(s1: String, s2: String) -> bool {
        let mut s1_character_set: HashSet<char> = HashSet::new();
        for ch in s1.chars() {
            s1_character_set.insert(ch);
        }
        for ch in s2.chars() {
            if !s1_character_set.contains(&ch) {
                println!("Impossible!");
                return false;
            }
        }
        true
    }
    pub fn update_id(p: i32, cnt: i32, length: i32) -> (i32, i32) {
        if p == length - 1 {
            return (0, cnt + 1);
        }
        return (p + 1, cnt);
    }
}
// @lc code=end
