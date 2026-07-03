// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

/*
we do bfs and return the last element of the level
*/
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![];
        let mut q: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        if let Some(r) = root {q.push_back(r)}

        while q.len() > 0 {
            let mut curr_level: Vec<i32> = vec![];
            let n = q.len();
            for i in 0..n {
                if let Some(node) = q.pop_front() {
                    let node_aux = node.borrow();
                    curr_level.push(node_aux.val);
                    if let Some(l) = node_aux.left.clone(){
                        q.push_back(l)
                    }
                    if let Some(r) = node_aux.right.clone(){
                        q.push_back(r)
                    }
                };
            }
            res.push(*curr_level.last().unwrap());
        } 
        return res; 
    }
}