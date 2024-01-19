/*
 * @lc app=leetcode.cn id=165 lang=rust
 *
 * [165] 比较版本号
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        let version1 = Self::pre_prepare(version1);
        let version2 = Self::pre_prepare(version2);
        let max_length = std::cmp::max(version1.len(), version2.len());
        for (v1, v2) in version1
            .iter()
            .chain(std::iter::repeat(&0))
            .take(max_length)
            .zip(
                version2
                    .iter()
                    .chain(std::iter::repeat(&0))
                    .take(max_length),
            )
        {
            match v1.cmp(v2) 
            {
                std::cmp::Ordering::Greater => return 1,
                std::cmp::Ordering::Less => return -1,
                _ => continue,
            }
        }
        0
    }
    fn pre_prepare(version: String) -> Vec<i32> {
        let version: Vec<&str> = version.split('.').collect();
        let version: Vec<i32> = version.into_iter().map(|x| x.parse().unwrap()).collect();
        version
    }
}
// @lc code=end
