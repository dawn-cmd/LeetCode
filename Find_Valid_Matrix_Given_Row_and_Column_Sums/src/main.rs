struct Solution {}
impl Solution {
    pub fn restore_matrix(row_sum: Vec<i32>, col_sum: Vec<i32>) -> Vec<Vec<i32>> {
        let mut row = row_sum;
        let mut col = col_sum;
        let mut ans = vec![];
        for i in 0..row.len() {
            ans.push(vec![]);
            for j in 0..col.len() {
                ans[i].push(row[i].min(col[j]));
                row[i] -= ans[i][j];
                col[j] -= ans[i][j];
            }
        }
        return ans;
    }
}
fn main() {
    println!("{:?}", Solution::restore_matrix(vec![3, 8], vec![4, 7]));
}
