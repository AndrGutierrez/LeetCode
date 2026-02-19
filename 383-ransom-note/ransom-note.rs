/*
each letter from magazine can be used only once in ransomnote

save all the magazine characters in hashmap then traverse ransomnote, if everything is true!!
*/
use std::collections::HashMap;
use std::collections::hash_map::Entry;

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut res = true;
        let mut magazine_map: HashMap<char, i32> = HashMap::new();
        for c in magazine.chars() {
            magazine_map.entry(c).and_modify(|v| *v += 1)
            .or_insert(1);
        }
        for c in ransom_note.chars(){
            match magazine_map.entry(c){
                Entry::Occupied(mut letter)=>{
                    let count = letter.get_mut();
                    *count -= 1;
                    if *count <0 {
                        return false;
                    }
                },
                Entry::Vacant(_)=>{return false}
            };
            // if magazine_map.entry(c) <= 0{
            //     return false;
            // }
        }
        return res
    }
}