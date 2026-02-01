/*
length of (int)
longest substring (sliding window?) without duplicate characters

first solution is brute force.


create window, 
if current already in the window, make left of the window the index of current
else right+=1

max_length = max(currentlenght, maxlength)

in the worst case scenario it's O(n) (all characters are the same)
*/
use std::collections::HashMap;
use std::cmp::max;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        //if s.len() as i32 == 0 {return 0};
        let mut left = 0;
        let mut right = 0;
        let n = s.len() as i32;
        let mut max_length = 0;
        let mut registered: HashMap<char, bool>= HashMap::new();
        let chars: Vec<char> = s.chars().collect();
        while right < n {

            let li = left as usize;
            let ri = right as usize;
            
            while registered.get(&chars[ri]).is_some() {
                    registered.remove(&chars[left as usize]);
                    left +=1;
            }
            registered.insert(chars[ri], true);
            right+=1;

            println!("{:?}, {:?}", left, right);
            max_length = max(right-left, max_length);


        }
        return max_length;
    }
}