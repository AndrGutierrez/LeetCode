/*
    The array is
    - Sorted, non decreasing
    - numbers[index1]+numbers[index2] == target, if index1 !=index2
    - targets and numbers can be negative
    
    trial = numbers[index1]+numbers[index2]
    if trial > target{
        if right > target {
            li+=1
        }
        else {
            ri-=1
        }
    }
    else {
        if left < target{
            li+=1
        }

    }

*/
impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let n: i32 = numbers.len() as i32;
        let mut ri: i32 = n-1;
        let mut li: i32 = 0;
        let mut left =  numbers[li as usize];
        let mut right =  numbers[ri as usize];

        while ri > li{
            left =  numbers[li as usize];
            right =  numbers[ri as usize];
            let mut trial = left+right;
            println!("{:?}, {:?}. {:?}", trial, li, ri);

            if trial == target{
                return vec![li+1, ri+1];
            }
            else {
                if trial >target{
                    if right > target{
                        ri-=1;
                    }
                    else if left<0 {
                        li+=1;
                    }
                    else {
                        ri-=1;
                    }
                }
                else{

                    li+=1
                }
            }
        }
        return vec![li+1, ri+1];

    }
}