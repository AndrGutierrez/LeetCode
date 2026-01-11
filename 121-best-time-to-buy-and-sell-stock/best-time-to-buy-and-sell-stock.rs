impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min = f64::INFINITY as i32;
        let mut max_profit = 0;
        for &price in prices.iter() {
            if price <= min { 
                min=price;
            }
            else if price-min > max_profit {
                max_profit =price-min;
            }

        }
        return max_profit;
    }
}