pub fn add_one(num: i32) -> i32 {
    let ans = (0..num).map(|n| n * n).filter(|n| (n & 1) == 0).sum();
    ans
}
