/*the problem asks for Ologn so probably binary search

so we start at the middle and if its bigger than its neighbors return, if the left element is bigger go to left
else go to right
*/
impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1{
            return 0
        }
        if nums[0] > nums[1]{
            return 0;
        }
        else if nums[n - 1] > nums[n - 2]{
            return (n - 1) as i32;
        }
        let mut low: i32 = 0;
        let mut high: i32 = (n - 1) as i32; 
        loop {
            let mut mid: usize = ((low + high) / 2) as usize;
            if nums[mid] > nums[mid.saturating_sub(1)] && nums[mid] > nums[mid + 1] {
                return mid as i32;
            }
            else if nums[mid] > nums[mid.saturating_sub(1)] {
                low = mid as i32;
            }
            else if nums[mid] < nums[mid.saturating_sub(1)] {
                high = mid as i32;
            }
        }

        return -1;
    }
}