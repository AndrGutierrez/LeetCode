/*
kth largest element

so we cannot sort because the orer changes and we need the kth

but if we make a max heap and pop we get it
*/

use std::collections::BinaryHeap;
impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut heap: BinaryHeap<i32> = BinaryHeap::from(nums);
        for i in 0..k {
            let val = heap.pop();
            match val {
                Some(v)=>{
                    if i as i32 == k - 1 {
                        return v;
                    }
                }
                _ =>{}
            }
        }
        return 0;
    }
}