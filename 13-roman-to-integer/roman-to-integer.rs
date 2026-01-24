/*
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').

s is guaranteed to have a valid roman number from 1 to 3999

res: int
let group be the group of subsequent equal characters


traverse backwards:
if number [i-1] >= number[i]
    add number[i-1] + number[i]
else:
    add number[i] - number[i-1]

XXIII





*/
use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let numbers: HashMap<char, i32> = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)

        ]);
        let arr: Vec<char>= s.chars().collect();
        let n: i32 = arr.len() as i32;
        let mut i: i32 = 0;
        let mut current: i32 = 0;
        let mut prev: i32 = 0;
        let mut res: i32 = 0;
        let mut next: i32 = 0;

        while i <= n-1  {
            current = *numbers.get(&arr[i as usize]).unwrap();
            if i +1 < n {
                next = *numbers.get(&arr[(i+1) as usize]).unwrap();
                if current >=next{
                    res+=current;
                    i+=1;
                }
                else {
                    res+=next-current;
                    i+=2;
                }
            }
            else {
                res+=current;
                i+=1;
            
            }

        }
        return res;  
    }
}