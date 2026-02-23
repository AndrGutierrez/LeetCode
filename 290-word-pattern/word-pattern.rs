use std::collections::HashMap;

/*

letter in pattern matches word in s

word in s matches letter

no letter can match two or more words

no word can match two or more patterns

traverse s

find word:
per each word go to next letter
if hashmap in letter already has word and is different from current word return false
if word already has matching letter
    if letter is different to current letter return false
else:
    save letter to word hashmap, repeat

save the letter to word hashmap


if 
*/
impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let pbytes = pattern.as_bytes();
        let sbytes = s.as_bytes();
        let mut n: usize = s.len();
        let mut i: usize = 0;
        let mut j: usize = 0;
        let increment: usize = 1;
        let mut pmap: HashMap<char, &str> = HashMap::new();
        let mut smap: HashMap<&str, char> = HashMap::new();

        let mut words: Vec<&str>= s.split_whitespace().collect();
        if words.len() != pattern.len() {return false}
        for (i, word) in words.iter().enumerate() {
            let c = pbytes[i] as char;
            let mut word_to_c = smap.entry(word).or_insert(c);

            if *word_to_c != c{
                return false;
            }
            let mut c_to_word = pmap.entry(c).or_insert(word);
            if c_to_word != word {
                return false;
            }
        }
        return true
    }
}