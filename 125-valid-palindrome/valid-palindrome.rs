impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        let mut start: usize = 0;
        let mut end: usize= chars.len()-1;

        while start<end {
            while (!chars[start].is_alphanumeric()) && start < end{
                start+=1;

            }
            while (!chars[end].is_alphanumeric()) && start<end {
                end-=1;
            }

            if !chars[start].eq_ignore_ascii_case(&chars[end]) {
                return false;
            }
            
            start += 1;
            if end > 0 { end -= 1; } 
        }           
        
        return true;
    }
}