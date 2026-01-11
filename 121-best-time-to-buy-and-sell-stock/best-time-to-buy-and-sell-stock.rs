impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // Inicializamos el precio mínimo con el valor más alto posible
        let mut min_price = i32::MAX;
        // La ganancia máxima empieza en 0
        let mut max_profit = 0;

        for price in prices {
            if price < min_price {
                // Si encontramos un precio más bajo, lo marcamos como nuevo punto de compra
                min_price = price;
            } else {
                // Si el precio es mayor al mínimo, calculamos la ganancia potencial
                let current_profit = price - min_price;
                if current_profit > max_profit {
                    max_profit = current_profit;
                }
            }
        }

        max_profit
    }
}