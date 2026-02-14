/*allocation is in place

rotate 90 degrees

so basically invert rows for columns

traverse columns,

matrix[i][j] is columns last element

reduce rows

matrix[i][j+1] columns last element,
when finished traversing columns, go to next row, and traverse next column
*/
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let mut current_row = 0;
        let aux = matrix.clone();
        for (i, row) in aux.iter().enumerate() {
            let mut last_in_column = (row.len() as i32) - 1;
            for (j, column) in row.iter().enumerate() {
                matrix[i][j] =  aux[last_in_column as usize][current_row as usize];
                last_in_column-=1;
            }
            current_row+=1;
        }
    }
}