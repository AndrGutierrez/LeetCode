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
        for i in 0..n {
            let si = s.chars().nth(i);
            let ti = t.chars().nth(i);

            match (si, ti) {
                (Some(sir), Some(tir))=>{
                    let already_mapped = tmap.entry(tir).or_insert(sir);
                    if *already_mapped != sir {
                        return false;
                    }
                    let replace: char = *map.entry(sir).or_insert(tir);
                    if replace != tir{
                        return false;
                    }                  
                },  
                _=>{}
            }
        }
        return res;
    }
}