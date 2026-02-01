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
if i use bfs

get the level

if the inverted level doesnt equal level return false

reversing an array is o(n) and that's depending the amount of levels, the amount of levels is limited though
*/
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut queue =  VecDeque::new();
        queue.push_back(root);
        let mut levels: Vec<Vec<i32>> = vec![];
        
        while queue.len() as i32 > 0 {
            let mut ql = queue.len() as i32; 
            let mut level: Vec<Option<i32>>= vec![];
            for i in 0..ql{
                let mut current = queue.pop_front().unwrap();
                match (current){
                    Some(c) =>{
                        let cref = c.borrow();
                        level.push(Some(cref.val));
                        queue.push_back(cref.right.clone());
                        queue.push_back(cref.left.clone());
                    },
                    None =>{level.push(None)}
                }
            }
                            let mut left = 0;
                let mut right = level.len() as i32 - 1;
                //println!("{:?}", level);
                while right > left {
                    let mut l = level[left as usize];
                    let mut r = level[right as usize];
                    //println!("{:?}, {:?}", l, r);

                    if l != r {return false}
                    left+=1;
                    right-=1
                }
            
        }
        return true;

    }
}