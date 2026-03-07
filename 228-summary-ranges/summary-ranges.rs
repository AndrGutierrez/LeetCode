/*
sorted and unique

range is ste of integers from a to b inclusive

smallest sorted list of ranges that covers all numbers

traverse the array until, the interval start in current, you find something that is bigger than current + 1
*/
impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
    
        let mut intervals: Vec<String> = vec![];
        let n = nums.len();
        if n == 0 {
            return intervals;
        }
        if n == 1 {
            return vec![nums[0].to_string()];
        }
        let mut start = nums[0];
        let mut end = nums[0];
        for i in 0..n - 1 {
            let num = nums[i];
            let finished = i+1 == n-1;
            let next = nums[i+1];


             if (next != num+1) {
                end = num;
                if start == end {
                    intervals.push(format!("{start}"));
                }
                else {
                    intervals.push(format!("{start}->{end}"));
                }
                start = next;
            }
            if finished{
                end = next;
                if start == end {
                    intervals.push(format!("{start}"));
                }
                else {
                    intervals.push(format!("{start}->{end}"));
                }
            }

        }
        return intervals;
    }
}