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
using BFS:

get the array of each level
reverse the array

rebuild the tree with that

or using dfs

convert to "standard"

then move to position

how do i rebuild the tree?
if levels are filled with null, 
left = (nextlevel[i]), right=nextlevel[i+1]
go next 

current.left = current.right
*/
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
use std::mem;
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut queue = VecDeque::new();
        let mut res = root.clone();
        queue.push_back(root);
        let mut levels: Vec<Vec<i32>> = vec![vec![]];
        while queue.len() as i32 > 0 {
            let mut ql = queue.len();
            let mut level: Vec<i32> = vec![];
            for i in 0..ql{
                let mut current = queue.pop_front().unwrap();
                match current {
                    Some(c) =>{
                        let mut cref= c.borrow_mut();
                        level.push(cref.val);
                        queue.push_back(cref.left.clone());
                        queue.push_back(cref.right.clone());
                        let node = &mut *cref;
                        mem::swap(&mut node.left, &mut node.right);
                    },
                    None => {}
                }
                

            }
            
        }
        return res;
    }
}