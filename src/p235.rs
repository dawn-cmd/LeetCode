/*
 * @lc app=leetcode.cn id=235 lang=rust
 *
 * [235] 二叉搜索树的最近公共祖先
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
struct Solution {}
// @lc code=start

use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let root_val = match root.as_deref() {
            Some(node) => node,
            None => return None,
        };
        let p_val = match p.as_deref() {
            Some(node) => node,
            None => return None,
        };
        let q_val = match q.as_deref() {
            Some(node) => node,
            None => return None,
        };
        if root_val.borrow().val > q_val.borrow().val
            && root_val.borrow().val > p_val.borrow().val
        {
            return Self::lowest_common_ancestor(root_val.borrow().left.clone(), p, q);
        } else if root_val.borrow().val < q_val.borrow().val
            && root_val.borrow().val < p_val.borrow().val
        {
            return Self::lowest_common_ancestor(root_val.borrow().right.clone(), p, q);
        } else {
            return root;
        }
    }
}
// @lc code=end
