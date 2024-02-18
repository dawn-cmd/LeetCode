/*
 * @lc app=leetcode.cn id=1627 lang=rust
 *
 * [1627] 带阈值的图连通性
 */
struct Solution;
// @lc code=start
struct UnionCombinationSet {
    fa: Vec<usize>,
}
impl UnionCombinationSet {
    fn new(n: usize) -> UnionCombinationSet {
        let mut tmp = vec![];
        for i in 0..n {
            tmp.push(i);
        }
        UnionCombinationSet { fa: tmp }
    }
    pub fn get_fa(&mut self, a: usize) -> usize {
        if self.fa[a] == a {
            return a;
        }
        self.fa[a] = self.get_fa(self.fa[a]);
        self.fa[a]
    }
    pub fn combine(&mut self, a: usize, b: usize) {
        if self.get_fa(a) == self.get_fa(b) {
            return;
        }
        let tmp = self.get_fa(a);
        self.fa[tmp] = self.get_fa(b);
    }
}
impl Solution {
    pub fn are_connected(n: i32, threshold: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = n as usize;
        let mut union_combination_set = UnionCombinationSet::new(n + 2);
        for z in threshold as usize + 1..=n - 1 {
            for j in 1..= (n / z) + 1 {
                if z * j > n {continue;}
                union_combination_set.combine(z, j * z);
            }
        }
        let mut ans = vec![];
        for query in queries {
            ans.push(
                union_combination_set.get_fa(query[0] as usize)
                    == union_combination_set.get_fa(query[1] as usize),
            );
        }
        ans
    }
}


// @lc code=end
fn main() {
    // Call the necessary functions or write the code logic here
    let tmp = Solution::are_connected(100, 1, vec![vec![1, 5], vec![19, 7], vec![100, 50]]);
    println!("{:?}", tmp);
}
