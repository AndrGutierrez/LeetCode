impl Solution {
    pub fn is_palindrome_old(s: String) -> bool {
        let n: usize= s.len() ;
        let mut start: usize = 0;
        let mut end: usize= n-1;

        let half: usize = n>>1;
        let mut first: char;
        let mut last: char;
        let mut valid = true;
        for i in 0..half {
            first = s.chars().nth(start).unwrap();
            last = s.chars().nth(end).unwrap();
            while (!first.is_alphanumeric() || first == ' ') && start <n-1 {
                start+=1;
                first = s.chars().nth(start).unwrap();

            }
            while (!last.is_alphanumeric() || last == ' ') && end > 0{
                end-=1;
                last= s.chars().nth(end).unwrap();
            }
                println!("{:?}, {:?}", first, last);

            if first.eq_ignore_ascii_case(&last) {
            }
            else {
                return false;

            }
            start+=1;
            end-=1;

        }           
        
        return valid;
    }
    pub fn is_palindrome(s: String) -> bool {
        let mut formatted = s.to_lowercase();
        formatted = formatted.chars().filter(|c| c.is_alphanumeric() && *c != ' ').collect();
        let n = formatted.len();
        let mut end = n-1;
        let mut start = 0;
        let mut evaluated_all= false;
        let mut first: char;
        let mut last: char;
        let mut valid= true;
        let half = n>>1;
        for i in 0..half {
            first = formatted.chars().nth(start).unwrap();
            last = formatted.chars().nth(end).unwrap();
            start+=1;
            end-=1;
            println!("{:?}, {:?}", first, last);
            if !first.eq_ignore_ascii_case(&last){
                return false;
            }
        }
        return valid;
    }
}