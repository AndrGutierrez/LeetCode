/*
only powers of I, X, C, M can be appended consecutively at most three times
1 <= num <=3999

divide number in characters

keep an eye on the multiples of 10 

the ith character in the order of n-i-1

evaluate character:
if character != 9 or character !=4
    value = character * order
    residual  = roman_number_trial-value

    while residual < 0 
        residual  = roman_number_trial-value
        try with smaller roman number
    while residual > 0 
        residual  = roman_number_trial-value

        add roman number trial to response

else if character == 4:
    evaluate roman_number_trials of 4 (IV, XL, CD) until match
    
else if character == 9:
    evaluate roman_number_trials of 9 (IX, XC, CM) until match


*/
use std::collections::HashMap;
impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let arr: Vec<char> = num.to_string().chars().collect();
        let n: i32 = arr.len() as i32;
        let numbers = [1000, 500, 100, 50, 10, 5, 1];
        let numbersMap: HashMap<i32, &str> = HashMap::from([
            (1,"I"),
            (5,"V"),
            (10,"X"),
            (50,"L"),
            (100,"C"),
            (500,"D"),
            (1000,"M")
        ]);
        let fours = [400,40,4];
        let foursMap: HashMap<i32, &str> = HashMap::from([
            (4,"IV"),
            (40,"XL"),
            (400, "CD")
        ]);
        let nines = [900,90,9];
        let ninesMap: HashMap<i32, &str> = HashMap::from([
            (9,"IX"),
            (90,"XC"),
            (900, "CM")
        ]);

        let mut res: String = "".to_string();
        for (i, c) in arr.iter().enumerate() {
            let index: u32 = i as u32;
            let base: i32 = 10;
            let order: u32 = base.pow(n as u32-index-1) as u32;
            
            let mut value = ((c.to_digit(10).unwrap())*order) as i32;
            if *c == '0' {
                continue;
            }
            if (*c != '4' && *c != '9'){
                let mut trial: i32 = numbers[0];
                let mut residual = value - trial;
                let mut j: i32 = 0;
                while residual != 0 {
                    j=0;
                    while residual < 0{
                        j+=1;
                        trial = numbers[j as usize];
                        residual = value - trial;
                    }

                    residual-=trial;
                    if residual < 0 {
                        value = residual+trial;
                        if value == 0{ break}

                    }

                    res.push_str(numbersMap[&trial]);

                }
                res.push_str(numbersMap[&trial]);


            }
            else if *c == '4'{
                let mut trial = fours[0];
                let mut residual = value - trial;
                let mut j = 0;
                while residual !=0{
                    j+=1;
                    trial = fours[j as usize];
                    residual = value - trial;    
                }
                res.push_str(foursMap[&trial])
            }
            else if *c == '9'{
                let mut trial = nines[0];
                let mut residual = value - trial;
                let mut j = 0;
                while residual !=0{
                    j+=1;
                    trial = nines[j as usize];
                    residual = value - trial;    
                }
                res.push_str(ninesMap[&trial])
            }
        } 
       return res;
    }
}