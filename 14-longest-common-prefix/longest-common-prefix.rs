/*
gets vector of trings

longest common prefix amongst all (sliding window?)
if no comon prefix, return ""
returns string

max size 200 strings of 200 characters each (a few, brute fore might be allowed)

edge cases=
[""]

base = first element

go next

compare each character with each base's until we find a new character

new base is the shortest found base

return base
*/
use std::cmp::min;
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut base: String = String::from(strs[0].clone());
        for s in strs.iter().skip(1){
            let schars: Vec<char> = s.chars().collect(); 
            let bchars: Vec<char> = base.chars().collect();

            let shortest_string: i32 = min(schars.len() as i32, bchars.len() as i32);
            let mut i: i32 = 0;
            let mut current_base: String = "".to_string(); 
            while i < shortest_string {
                let idx = i as usize;
                if schars[idx] != bchars[idx]{
                    break;
                }
                else {
                    current_base.push(schars[idx]);
                }
                i+=1
            }
            base = current_base;
        }
        return base;
    }
}