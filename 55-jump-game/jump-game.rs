impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut max_reachable: i32 = 0;
        for (index,&num) in nums.iter().clone().enumerate() {
            let i = index as i32;
            if max_reachable >= nums.len()as i32-1 {
                return true
            }
            if num == 0 && max_reachable <= i{
                return false
            } 
            if num + i > max_reachable{
                max_reachable = num+i;
            }

        }
        return true
    }
}