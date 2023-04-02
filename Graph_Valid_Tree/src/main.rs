impl Solution {
    pub fn transfer(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = vec![vec![]; n as usize];
        for edge in edges {
            ans[edge[0] as usize].push(edge[1]);
            ans[edge[1] as usize].push(edge[0]);
        }
        ans
    }
    pub fn dfs(cur: i32, edges: &Vec<Vec<i32>>, visited: &mut Vec<bool>) {
        if visited[cur as usize] {
            return;
        }
        visited[cur as usize] = true;
        for next in &edges[cur as usize] {
            Solution::dfs(*next, edges, visited);
        }
    }
    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {
        if edges.len() as i32 != n - 1 {
            return false;
        }
        let edges = Solution::transfer(n, edges);
        let mut visited = vec![false; n as usize];
        Solution::dfs(0, &edges, &mut visited);
        return !visited.contains(&false);
    }
}
struct Solution;
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_tree() {
        let edges = vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 4]];
        assert_eq!(Solution::valid_tree(5, edges), true);

        let edges = vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![1, 3], vec![1, 4]];
        assert_eq!(Solution::valid_tree(5, edges), false);

        let edges = vec![vec![0, 1], vec![0, 2], vec![2, 3], vec![2, 4]];
        assert_eq!(Solution::valid_tree(5, edges), true);

        let edges = vec![vec![0, 1], vec![0, 2], vec![1, 3], vec![2, 4]];
        assert_eq!(Solution::valid_tree(5, edges), true);
    }
}
fn main() {
    let edges = vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 4]];
    println!("{}", Solution::valid_tree(5, edges));
}
