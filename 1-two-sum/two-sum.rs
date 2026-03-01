/*
there's only ONE solution, cannot use the same element twice

first thing is brute force but thats like o n^2 or smth like thath, too much

i could sort but thats nlogn this seems to require o(n)

and numbers and target can be negative

target = current + x

x = target - current

search in hashmap current, if it doesnt existst, save its index,

get target- current, if theres an x in the hashmap with that value return current index and that items valuie
*/

use std::collections::HashMap;
impl Solution {
    pub fn two_sum(mut nums: Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        let unit: usize = 1;
        let mut res: Vec<i32> = vec![];
        let mut map: HashMap<i32, usize> = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            let x = map.get(&(target-num));
            match x {
                Some(value)=>{
                    return vec![*value as i32, i as i32];
                }
                _=>{}
            } 
            let entry = map.entry(*num).or_insert(i);

        }      
        return vec![];
    }
}