/*
direction = 1
left = i
right = m-1

top = j
bottom = n-1
add the ith element from left to right , add i+=direction,  
if i == right, direction*=-1, swap left and right, now move in columns
add the jth element from top to bottom , add j+=direction,
if j == bottom, move in rows


if we gave a whole lap, then left +=1, right -=1, top+=1, bottom -=1
*/
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut m: i32 = matrix[0].len() as i32;
        let mut n: i32 = matrix.len() as i32;

        let mut direction = 1;

        let mut visited = vec![];
        let mut j = 0;
        let mut i = 0;
        let mut total_items: i32=  m*n;

        let mut row_len = m ;
        let mut col_len = n;
        let mut ciclos = 0;
        while (visited.len() as i32) < total_items{
            // rows
            let mut vr = 0;
            let mut vc = 0;
            loop {
                if vr>=row_len {
                    j-=direction;
                    break;
                }
                //println!("{j}");

                let item = matrix[i as usize][j as usize];
                //println!("{item}");
                visited.push(item);
                if (visited.len() as i32) >= total_items {
                    break
                }
                j+=direction;
                vr+=1;
            }
                            if (visited.len() as i32) >= total_items {
                    break
                }
            //columns
            //println!("###");
            loop {

                i+=direction;
                vc+=1;
                if vc >= col_len {
                    i-=direction;
                    break;
                }
                let item = matrix[i as usize][j as usize];
                //println!("{item}");
                
                visited.push(item);
                                if (visited.len() as i32) >= total_items {
                    break
                }

            }
            direction*=-1;
            j+=direction;
            row_len-=1;
            col_len-=1;

            // break;
           // println!("###");
            // ciclos+=1;
            // if ciclos % 2==0{
            //     row_len-=1;
            //     col_len-=1;
            //     // if m > 3{
            //     //     row_len-=2;
            //     // }
            //     // else {
            //     //     row_len-=1;
            //     // }
            //     // if n > 3{
            //     //     col_len-=2;
            //     // }
            //     // else {
            //     //     col_len-=1;
            //     // }
// 
            //     i+=direction;
            //     j+=direction;
            // println!("{i}, {j}");

//            }

        }
        return visited;
    }
}