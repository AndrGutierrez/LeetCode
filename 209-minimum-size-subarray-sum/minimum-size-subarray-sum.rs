
use std::cmp::min;
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut window_size: i32 = 4;
        let mut min_window_size: i32 = 0;
        let mut left: i32 = 0;
        let mut right: i32 = 0;
        let n: i32 = nums.len() as i32;
        while right <= n {
            loop {
                let mut sum: i32 =0;
                for j in left..right {
                    sum+=nums[j as usize];
                }

                if sum >= target{
                    let wsize= right-left;
                    if min_window_size == 0{
                        min_window_size = wsize;
                    }
                    else {
                        min_window_size = min(min_window_size, wsize);
                    }
                    left+=1;
                }            
                else {
                    right+=1;
                    break
                }
            }
        }
        return min_window_size;
    }
}