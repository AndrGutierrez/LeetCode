impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut prefix: Vec<i32>= Vec::<i32>::new();
        let mut suffix: Vec<i32> = Vec::<i32>::new();
        let mut res: Vec<i32> = Vec::<i32>::new();
        let mut p:i32= 1;
        let mut s:i32 = 1;
        let n: i32 = nums.len() as i32;
        for i in 0..n {
            prefix.push(p);
            suffix.push(s);
            
            p = p*nums[i as usize];
            s = s*nums[(n-i-1) as usize];
        }
        for i in 0..n{
            res.push(prefix[i as usize]*suffix[(n-i-1) as usize]);
        }

        return res;
    }
}