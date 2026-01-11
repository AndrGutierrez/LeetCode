use std::collections::VecDeque;
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profits: Vec<i32> = Vec::new();
        let mut min:i32 = f64::INFINITY as i32;
        for price in prices { 
            if price < min{
                min= price;
            }
            else if price>min{
                let profit = price-min;
                profits.push(profit);
                min=price;
            }
        }
        return profits.iter().sum();
    }
}