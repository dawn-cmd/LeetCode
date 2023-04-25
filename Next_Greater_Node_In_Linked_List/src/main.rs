use std::{collections::BinaryHeap, cmp::Reverse};

//Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}
impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
struct Solution {}
impl Solution {
    pub fn next_larger_nodes(head: Option<Box<ListNode>>) -> Vec<i32> {
		let mut cur = head;
		let mut count = 0;
		let mut ans = vec![];
		let mut rest: BinaryHeap<(Reverse<i32>, i32)> = BinaryHeap::new();
		while let Some(node) = cur {
			while let Some((val, id)) = rest.peek() {
				if (*val).0 >= node.val {
					break;
				}
				ans[*id as usize] = node.val;
				rest.pop();
			}
			ans.push(0);
			rest.push((Reverse(node.val), count));
			count += 1;
			cur = node.next;
		}
		return ans;
    }
}
fn main() {
    println!("Hello, world!");
}
