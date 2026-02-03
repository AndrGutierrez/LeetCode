/* aguja en un pajar
el indice de la primera aguja en el pajar, o -1 si no se encuentra

la ajuga es un string, 

sliding window

if the current character if the same as haystacks ith character, i+=1
if i >= len(needle): return left as the index of the window

 continue
else: left = right, go next

return -1

*/

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let n = haystack.len() as i32;
        let hchars: Vec<char>= haystack.chars().collect();
        let nchars: Vec<char> = needle.chars().collect();
        let mut i = 0;
        while right < n{
            let current = hchars[right as usize];
            let needlechar =nchars[i as usize];
            if  current ==  needlechar{
                i+=1;
                if i >= nchars.len(){
                    return left;
                }
                right+=1;

            }
            else {
                loop {
                    left+=1;
                    if left >=n {return -1}
                    if !(hchars[left as usize] !=  nchars[0 as usize]) {break}
                }
                right = left;

                i=0;

            }

        }
        return -1;
    }
}