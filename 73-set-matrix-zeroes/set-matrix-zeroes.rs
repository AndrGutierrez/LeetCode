/*
max 200*200
min 1*1
number fit in a 32 bit integer, but i guess the point is that they are BIG

constant space complexity is the best solution

in place

traverse the whole matrix, save the indexes of 0 in row and column, check that's not repeated, then run again and replace
*/
use std::collections::HashMap;
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut rows_with_zeros: HashMap<usize, bool> = HashMap::new();
        let mut columns_with_zeros: HashMap<usize, bool> = HashMap::new();

        // the worst case here is there's no 0's, so we wont handle skip because we're looking for big O, though it could be optimized
        for (i, row) in matrix.iter().enumerate() {
            for (j, column) in row.iter().enumerate() {
                if matrix[i][j] == 0 {
                    rows_with_zeros.entry(i).or_insert(true);
                    columns_with_zeros.entry(j).or_insert(true);

                }
            }
        }
        
        for i in 0..matrix.len() {
            for j in 0..matrix[i].len() {
                match (rows_with_zeros.get(&i), columns_with_zeros.get(&j)) {
                    (Some(val), _) | (_, Some(val))  => {
                        matrix[i][j] = 0;           
                    },
                    _ =>{}
                }
            }
        }
        // println!("{:?}", rows_with_zeros);
        // println!("{:?}", columns_with_zeros);

    }
}