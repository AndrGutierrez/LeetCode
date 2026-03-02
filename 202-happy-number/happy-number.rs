/*
repeat until the sum of squares equals 1, it's all positive

register the squares of each digit from 0 to 9 in a hashmap

return true if happy return false if not

so happy numbers are the ones whos sum is multiples is power of 10

or if it includes 1 and the rest ar 0s which is the same,

get the sum, if

for 112, 222, 444, 

n1^2 + n2^2 + n3^2 + ... is power of 10
*/

use std::collections::HashMap;
impl Solution {
    pub fn is_happy(mut n: i32) -> bool {
        let mut appearences: HashMap<i32, i32>= HashMap::new();
        loop {
            let string: String = n.to_string();
            let chars = string.chars();
            let mut sum: i32 = 0;
            for c in chars {
                let cint = c.to_digit(10).unwrap();
                sum+= cint.pow(2) as i32;
            }
            if sum == 1{
                return true;
            }
            let number = appearences.entry(sum).or_insert(0);
            *number +=1;
            if *number > 1{
                return false;
            }
            n=sum;
        } 
        return true
    }
}