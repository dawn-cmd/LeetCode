// * @lc app=leetcode.cn id=535 lang=rust
//  *
//  * [535] TinyURL 的加密与解密

// @lc code=start
use std::collections::HashMap;
struct Codec {
    url_map: HashMap<usize, String>,
    url_count: usize,
}
/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Self {
            url_map: HashMap::new(),
            url_count: 0,
        }
    }

    // Encodes a URL to a shortened URL.
    fn encode(&mut self, long_url: String) -> String {
        self.url_count += 1;
        self.url_map.insert(self.url_count, long_url);
        self.url_count.to_string()
    }

    // Decodes a shortened URL to its original URL.
    fn decode(&self, short_url: String) -> String {
        let short_url = match short_url.parse::<usize>() {
            Ok(num) => num,
            Err(_) => 0,
        };
        self.url_map.get(&short_url).unwrap().clone()
    }
}

// @lc code=end
