/*
 * @lc app=leetcode.cn id=787 lang=rust
 *
 * [787] K 站中转内最便宜的航班
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let ans = Self::bellman_ford(n, flights, k, src, dst);
        if ans > 0x3f3f3f3f / 2 {
            -1
        } else {
            ans
        }
    }
    pub fn bellman_ford(n: i32, flights: Vec<Vec<i32>>, k: i32, src: i32, dst: i32) -> i32 {
        let mut dist = vec![0x3f3f3f3f; n as usize];
        dist[src as usize] = 0;
        for _ in 0..=k {
            let clone = dist.clone();
            for flight in flights.iter() {
                let (from, to, cost) = (flight[0] as usize, flight[1] as usize, flight[2]);
                dist[to] = dist[to].min(clone[from] + cost);
            }
        }
        println!("{:?}", dist);
        dist[dst as usize]
    }
}
// @lc code=end
