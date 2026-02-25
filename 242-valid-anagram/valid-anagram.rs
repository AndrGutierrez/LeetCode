use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut smap = HashMap::new();
        if s.len() != t.len(){
            return false;
        }
        for c in s.chars() {
            let mut entry = smap.entry(c).or_insert(0);
            *entry+=1;
        }

        for c in t.chars() {
            let mut entry = smap.entry(c).or_insert(0);
            *entry -= 1;
            if *entry < 0 {
                return false;
            }
        }
        //println!("{:?}", smap);
        return true
    }
}