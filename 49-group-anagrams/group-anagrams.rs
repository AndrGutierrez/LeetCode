/*
I could sort the characters but thats often nlogn

traverse each str, 

lenght of strings is fairly small, so lets give it a try... though there can be repeated characters... doesnt matter


sort, get or insert into the hashmap, add to a different hashmap and then return only the values
*/

use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut anagrams: HashMap<String, Vec<String>> = HashMap::new();
        for w in strs {
            let mut chars: Vec<char> = w.chars().collect();
            chars.sort();
            let sorted: String = chars.into_iter().collect();
            let mut anagram = anagrams.entry(sorted).or_insert(vec![]);
            anagram.push(w);
        }
        let res: Vec<Vec<String>> = anagrams.into_values().collect();

        return res;
    }
}