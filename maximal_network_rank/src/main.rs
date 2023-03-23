struct Solution {}
impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let mut h = std::collections::HashMap::new();
        let mut cnt_roads = vec![0; n as usize];
        for road in &roads {
            cnt_roads[road[0] as usize] += 1;
            cnt_roads[road[1] as usize] += 1;
            h.insert((road[0], road[1]), 1);
            h.insert((road[1], road[0]), 1);
        }
        let mut ans = -1;
        for i in 0..n as usize {
            for j in i + 1..n as usize {
                ans = ans.max(
                    cnt_roads[i] + cnt_roads[j]
                        - if h.contains_key(&(i as i32, j as i32)) {
                            1
                        } else {
                            0
                        },
                );
            }
        }
        return ans;
    }
}
fn main() {
    println!("{}", Solution::maximal_network_rank(4, vec![vec![0, 1], vec![0, 3], vec![1, 2], vec![1, 3]]));
}
