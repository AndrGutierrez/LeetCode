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
return i32
maximum depth of three
doesn't require backtracking
doesn't require going branch by branch

add n to queue (1)
add left and right to queue (2)
add left and right of left (3)
add left and right of right (3)

things i have:
the lenght of the queue

*/
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut queue = VecDeque::new();
        queue.push_back(root);
        let mut depth = -1;
        let mut levels: Vec<Vec<TreeNode>> = vec![];
        while queue.len() as i32 > 0 {
            let current_level_size = queue.len() as i32;
            depth+=1;
            for i in 0..current_level_size{
                match queue.pop_front().unwrap(){
                    Some(n)=>{
                        let node = n.borrow();
                        queue.push_back(node.left.clone());
                        queue.push_back(node.right.clone());
                    }
                    None => continue
    
                }

            }
        }

        return depth;
    }
}