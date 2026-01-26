/*
this is done intil right is reached

then it gets the sum from right to left inside a loop, thats also a loop, the bigest the ragne the hicher the m 

*/
use std::cmp::min;
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut window_size: i32 = 4;
        let mut min_window_size: i32 = 0;
        let mut left: i32 = 0;
        let n: i32 = nums.len() as i32;
        for right in 0..n {
            let mut sum: i32 = nums[left as usize..(right+1) as usize].iter().sum();
            while sum >= target {
                let wsize: i32 = right -left +1;
                if min_window_size == 0{
                    min_window_size = wsize;
                }
                else {
                    min_window_size = min(min_window_size, wsize);
                }
                // min_window_size = right - left +1;
                sum -=nums[left as usize];
                left+=1;
            }            
        }
        return min_window_size;
    }
}