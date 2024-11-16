struct Solution;
impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        let mut q = vec!["".to_string()];
        for _ in 0..n {
            let mut new_q = vec![];
            for s in q {
                if s.len() == 0 || s.chars().last().unwrap() != '0' {
                    let mut s1 = s.clone();
                    s1.push('0');
                    new_q.push(s1);
                }
                let mut s2 = s.clone();
                s2.push('1');
                new_q.push(s2);
            }
            q = new_q;
        }
        q
    }
}
fn main() {}
