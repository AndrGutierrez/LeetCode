/*
make a queue, traverse the array, 

if opens, insert element in the queue, if closes, popleft, if any of them doesnt match the closing, return false
*/
use std::collections::{HashMap, VecDeque};
impl Solution {
    pub fn is_valid(s: String) -> bool {

        let chars: Vec<char> = s.chars().collect();
        let opens: HashMap<char, char> = HashMap::from([
            ('{', '}'),
            ('(', ')'),
            ('[', ']'),
        ]);
        let closes: HashMap<char, char> = HashMap::from([
            ('}', '{'),
            (')', '('),
            (']', '['),
        ]);
        let mut q: VecDeque<char> = VecDeque::new();
        for c in chars {
            if opens.get(&c).is_some(){
                q.push_back(c);
            }
            else if closes.get(&c).is_some(){
                let op = closes.get(&c).unwrap();
                if q.len() ==0 {
                    return false
                }
                let start = q.pop_back().unwrap();

                if *op != start{
                    return false;
                }
            }
        }
        if q.len()>0{
            return false
        }
        return true
    }
}