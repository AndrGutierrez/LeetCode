use std::collections::HashMap;
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let mut c: HashMap<i32, i32>= HashMap::new();
        for &amount in citations.iter() {
            let mut m = amount;
            let n = citations.len() as i32;
            if amount >=n{m=n}
            for i in 0..m+1{
                let mut number = c.entry(i).or_insert(0);
                *number+=1;
            }
            
        }

        let mut max=0;
        for (key, value) in c.iter(){
            if key >&max{
                if (value>=key) {
                    max=*key;
                }
            }
        }
        return max;
    }
}