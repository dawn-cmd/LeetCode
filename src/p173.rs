/*
 * @lc app=leetcode.cn id=173 lang=rust
 *
 * [173] 二叉搜索树迭代器
 */
// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
// @lc code=start
use std::{borrow::Borrow, cell::RefCell, rc::Rc};

struct BSTIterator {
    path: Vec<Rc<RefCell<TreeNode>>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BSTIterator {
    fn push_left(&mut self, node: Option<Rc<RefCell<TreeNode>>>) {
        if let Some(current) = node {
            self.push_left(current.borrow_mut().left.take());
            self.path.push(current);
        }
    }

    fn new(&mut self, root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut iter = Self { path: vec![] };
        iter.push_left(root);
        iter
    }

    fn next(&mut self) -> i32 {
        let ans = self.path.pop();
        if let Some(mut node) = ans {
            self.push_left(node.borrow_mut().right.take());
            return node.borrow_mut().val;
        }
        -1
    }

    fn has_next(&self) -> bool {
        !self.path.is_empty()
    }
}

// /**
//  * Your BSTIterator object will be instantiated and called as such:
//  * let obj = BSTIterator::new(root);
//  * let ret_1: i32 = obj.next();
//  * let ret_2: bool = obj.has_next();
//  */
// @lc code=end
