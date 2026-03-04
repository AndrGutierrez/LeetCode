/*
{
    x = y
    
}
*/
use std::collections::HashMap;
impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut map: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut res = false;
        for (i, num) in nums.iter().enumerate(){
            let mut e = map.entry(*num).or_insert(vec![]);
            e.push(i as i32);
            
        }
        for value in map.values(){
            if value.len() > 1 as usize{
                for i in 1..value.len() {
                    if value[i] - value[i - 1 as usize] <=k{
                        return true
                    }
                }
            }
        } 
        return res
    }
}