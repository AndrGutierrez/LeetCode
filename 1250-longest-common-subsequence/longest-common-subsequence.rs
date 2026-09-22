/*
longest common subsequence

I think this can be dp because we can divide it into subproblems?
 besides I already solved one in python, input size suggest O(n^2) solution

*/
use std::cmp::max;
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let m = text1.len()+1;
        let n = text2.len()+1;
        let mut dp: Vec<Vec<i32>>= vec![vec![0;  n]; m];
        let mut res = 0;
        for i in 1..m{
            for j in 1..n{
                if text1.chars().nth(i-1) == text2.chars().nth(j-1){
                    dp[i][j] = dp[i-1][j-1]+1;               
                }
                else{
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]);

                }

            }
        }
        for row in 0..m {
            println!("{:?}",dp[row]);
        }

        res = dp[m-1][n-1];
            println!("{:?}",res);

        return res
    }
}