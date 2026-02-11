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
reconstruct binary tree based in inorder and postorder

unique values (important)

guaranteed to be inorder and postorder

buildtree: 
    if theres no rightsubtree
    if elements is empty return none
    rightsubtree is the elements at the right of root
    leftsubtree is the elements at the left of root

    root.val = rootval
    root.right = buildtree(rightsubtree)
    root.left = buildtree(leftsubtree)
    return root
*/
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;
impl Solution {
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let n = postorder.len() as i32;
        let mut indexmap: HashMap<i32, i32> = inorder.iter().enumerate().map(|(i, &v)| (v, i as i32)).collect();
        let mut left: i32 = 0;
        let mut right: i32 = (n-1);
        let mut postorderclone = postorder.clone();
        let root =  Solution::build(left, right, &mut postorderclone, indexmap.clone());
        return root;
    }
    pub fn build(left: i32, right: i32, postorder: &mut  Vec<i32>, indexmap: HashMap<i32, i32>)-> Option<Rc<RefCell<TreeNode>>> {
        
        if left > right {
            return None
        }
        let rootval = postorder.pop(); 
        // println!("{:?}, {:?}, {:?}", left, right, rootval);
        
        match rootval {
            Some(r) => {
                let mut node = TreeNode::new(r);
                let idx: i32 = *indexmap.get(&r).unwrap();

                node.right = Solution::build(idx+1, right,  postorder, indexmap.clone());
        // println!("{:?}", postorder);

                node.left = Solution::build(left, idx-1, postorder, indexmap.clone());
                let root = Some(Rc::new(RefCell::new(node)));

                return root;
            }
            None=>{
                return None
            }
        }        

    }
}
