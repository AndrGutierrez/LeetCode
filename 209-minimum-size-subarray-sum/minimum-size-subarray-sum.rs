/*
- Positive integers
- Positive target
- MINIMAL length (greedy?)
- return LENGTH of the min_sub
- min_sub is minimal subarray in nums such that sum(subarray) is GREATER OR EQUAL to target
- if doesnt exist, return 0 
- target > 0
- all numbers > 0

make a window of  size two
got to ith element  to ith+window size - 1

if the sum of the elements in the window equal target, regurn window size

else, slide the window

if window size<=n
    if not found increase window size
else;
    return 0
*/
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