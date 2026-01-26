/*
two pointers:
left 0 
right n-1

theres a space of 1 unit between each line 

area = min(left, right) * max(left, right)-min(left, right)
area = max(area,max_area)
if left < right 
    go next left
else 
    go back right

height >=0
if height == 0
*/

use std::cmp::{min, max};
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let n: i32 = height.len() as i32;
        let mut li = 0;
        let mut ri = n-1;
        let mut max_area = 0;
        while li < ri {
            let left = height[li as usize];
            let right = height[ri as usize];
            let current_area = min(left, right) * (ri-li);
            println!("{:?}, {:?}, {:?}", current_area, li, ri);
            max_area = max(current_area, max_area);
            if left > right{ 
                ri-=1;
            }
            else {
                li+=1;
            }

        }
        return max_area
    }
}