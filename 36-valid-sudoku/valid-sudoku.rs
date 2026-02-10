/* 
IMPORTANT: only filled cells must be validated

each row contains the digits 1 to 9 without repetition
same for columns

all sub boxes must contain the digits 1 to 9 without repetition

greedy?

worst caes is everything is filled

if I go by brute force the complexity is something like O(n³)

Its always the same board so time complexity shouldnt be that important

check rows,
check columns

check from nrows to nrows+2 in rows, if repeated_row or repeated_square return False,
check from ncolumns to ncolumns+2 in columns if repeated_column or repeated_square return False

each time you got to a square reset repeatd_square, each time you finish the whole row reset it, same for column
*/
use std::collections::HashMap;
impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut valid = true;
        let mut nrows = 0;
        let mut ncolumns = 0;
        let mut visited_in_rows: HashMap<i32, HashMap<char, bool>> = HashMap::from([
            (0, HashMap::new()),
            (1, HashMap::new()),
            (2, HashMap::new()),
            (3, HashMap::new()),
            (4, HashMap::new()),
            (5, HashMap::new()),
            (6, HashMap::new()),
            (7, HashMap::new()),
            (8, HashMap::new()),
        ]);
        let mut visited_in_columns: HashMap<i32, HashMap<char, bool>> = HashMap::from([
            (0, HashMap::new()),
            (1, HashMap::new()),
            (2, HashMap::new()),
            (3, HashMap::new()),
            (4, HashMap::new()),
            (5, HashMap::new()),
            (6, HashMap::new()),
            (7, HashMap::new()),
            (8, HashMap::new()),
        ]);
        /* for while nrows < 9{
            while ncolumns <9 {
                for j in ncolumns..(ncolumns+1){
                    let mut num = board[i][j];
                    if num == '.'{
                        // continue;
                    }
                    print!("{:?}", num);
                    // print!("({:?}, {:?}) ", i, j);


                }
                ncolumns+=1;
                nrows+=

            }
            println!("");
            ncolumns = 0;
        }*/
        while ncolumns < 9 {
            let mut visited_in_square: HashMap<char, bool> = HashMap::new();

            for i in nrows..nrows+3{
                let mut row: &mut HashMap<char, bool> = visited_in_rows.get_mut(&(i as i32)).unwrap();

                for j in ncolumns..ncolumns+3{
                    let mut column: &mut HashMap<char, bool> = visited_in_columns.get_mut(&(j as i32)).unwrap();

                    let mut num = board[i][j];
                    if num == '.' {continue}
                    match visited_in_square.get(&num){
                        Some(_)=> return false,
                        None => visited_in_square.insert(num, true)

                    };

                    match row.get(&num) {
                        Some(_) => return false,
                        None => row.insert(num, true)
                    };

                    match column.get(&num) {
                        Some(_) => return false,
                        None => column.insert(num, true)
                    };


                }
            }
            nrows+=3;

            if nrows >=9 {
                nrows= 0;
                ncolumns+=3;
            }
        }
        return valid;
    }
}