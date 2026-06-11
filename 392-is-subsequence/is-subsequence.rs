/*
ok i think we can do this in O(n) time by keeping a pointerin thelatest not found letter and a pointerin t, if we traverse s we're done
*/
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut left: usize = 0;
        let right: i32 = 0;
        let target = s.len();
        if target == 0 {
            return true
        }
        for c in t.chars() {

            let current_s: char = s.chars().nth(left).unwrap();

            if current_s == c {

                left+=1;
                if left == target {
                    return true
                }

            }
        }
        return false;
    }
}