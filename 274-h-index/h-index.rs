use std::collections::HashMap;
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let mut c: HashMap<i32, i32>= HashMap::new();
        for amount in citations {
            for i in 0..amount+1{

                let mut number = c.entry(i).or_insert(0);

                *number+=1;

            }
        }
        println!("{:?}", c);

        let mut max=0;
        let mut biggest_key = 0;
        for (key, value) in c.iter(){
            if *key > biggest_key {biggest_key =*key}
            if key >&max{
                if (value>=key) {
                    max=*key;
                }
                else {
                }

            }
        }
        if (max==0){return biggest_key}        
        return max;
    }
}