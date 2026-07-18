/*
2 to 9, all possible combinations, return answer in any order. 

Digits is of len 4 at most so we can assume this is heavy, brute forcing the solution, using backtracking

ok so how was backtracking again?

so we see it as a tree dfs, doing and undoing a solution again and again

ok so.... we have the options of the string, we pass the next item of the string and add 

more specifically, we create a hashmap with the letters for each digit.

for each possible letter we recursively call backtrack for the next letter of the string, and push to the res

we stop if we don't have more string to traverse
*/

use std::collections::HashMap;
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let mut res: Vec<String> = vec![];
        let n = digits.len();
        let letter_map: HashMap<char, Vec<char>> = HashMap::from([
            ('2', vec!['a', 'b', 'c']),
            ('3', vec!['d','e','f']),
            ('4', vec!['g','h','i']),
            ('5', vec!['j','k','l']),
            ('6', vec!['m','n','o']),
            ('7', vec!['p','q','r', 's']),
            ('8', vec!['t','u','v']),
            ('9', vec!['w','x','y', 'z']),

        ]);
        fn backtrack (sequence: &mut Vec<char>, i: usize, res: &mut Vec<String>, digits: &str, n: usize, letter_map: &HashMap<char, Vec<char>>) {
            if i >= n {
                res.push(sequence.iter().collect());
                return
            }
            let options = &letter_map[&digits.chars().nth(i).unwrap()];
            for letter in options {
                sequence.push(*letter);
                backtrack(sequence, i + 1, res, digits, n, letter_map);
                sequence.pop();
            }
        }; 
        backtrack(&mut vec![], 0 as usize, &mut res, &digits as &str, n, &letter_map);
        return res;
    }
}