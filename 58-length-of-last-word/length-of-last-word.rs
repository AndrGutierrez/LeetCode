/*
- substring: sliding window?
- returns i32, length of last word
- is current a space?
    yes:
        wsize = 0
        go next
    no: wsize+=1
*/
impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut window_sizes: Vec<i32> = Vec::<i32>::new();
        let mut chars: Vec<char> = s.chars().collect();
        let mut current_size = 0;
        for c in chars {
            if c == ' '{
                current_size = 0;
            }
            else {
                current_size+= 1;
            }
            if current_size > 0{
                window_sizes.push(current_size);
            }

        }
        let mut last = window_sizes.len() as i32 - 1;
        return window_sizes[last as usize];
    }
}