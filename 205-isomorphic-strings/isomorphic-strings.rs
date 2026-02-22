use std::collections::HashMap;

/*
get character, in s and t,
if its not in hashmap
     replace s for t and save in hash map
else: get from hashmap

if its different return false

*/
impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut map: HashMap<char, char> = HashMap::new();
        let mut tmap: HashMap<char, char> = HashMap::new();

        let characters = s.chars();
        let mut res = true;
        let n: usize = s.len();
        let sbytes = s.as_bytes();
        let tbytes = t.as_bytes();

        for i in 0..n {
            let sir = sbytes[i] as char;
            let tir = tbytes[i] as char;


            let already_mapped = tmap.entry(tir).or_insert(sir);
            if *already_mapped != sir {
                return false;
            }

            let replace: char = *map.entry(sir).or_insert(tir);
            if replace != tir{
                return false;
            }                  
        }
        return res;
    }
}