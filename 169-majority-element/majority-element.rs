use std::collections::HashMap;

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut elements: HashMap<i32,i32>= HashMap::new();
        for num in nums {
            elements.entry(num).and_modify(|count| *count+=1).or_insert(1);
        }
        let response =elements.iter().max_by_key(|entry| entry.1);
        if response.is_some(){
           return *response.unwrap().0;
        }
        return 0;
    }
}
