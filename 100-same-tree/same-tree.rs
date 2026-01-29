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
find shortest path? no
do i have to check all the nodes?

the first solution: convert both trees to array, then compare both arrays

max nodes 100 (recursion allowed)

nodes can be negative

BFS probably

if node is None append null

though we can compare the queues ...
or level by level
*/
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut arr: Vec<i32> =  Vec::<i32>::new();
        let mut queue = VecDeque::new();

        let mut res = true;
        queue.push_back((p, q));
        while let Some((que_p, que_q)) =  queue.pop_front() {
            match (que_p, que_q) {
                (None, None) => continue,
                (Some(qp), Some(qq)) => {
                    let qref = qq.borrow();
                    let pref= qp.borrow();
                    if pref.val != qref.val {
                        return false;
                    }
                    queue.push_back((pref.left.clone(), qref.left.clone()));
                    queue.push_back((pref.right.clone(), qref.right.clone()))
                }
                _=> return false

                }
        }

        return res;

    }

}