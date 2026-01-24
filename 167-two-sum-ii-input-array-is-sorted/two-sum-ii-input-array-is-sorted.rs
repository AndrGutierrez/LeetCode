/*
    The array is
    - Sorted, non decreasing
    - numbers[i]<numbers[i+1]
    - numbers[index1]+numbers[index2] == target, if index1 !=index2
    - if numbers[i]>target{
        next
    } 
    - traversing the array backwards {
        if numbers[i]+numbers[i-1] > target {
            i-=1;

        }
        elif numbers[i]
    }

    numbers can be negative

    index >= 1
    return [index1 + 1, index2+1]
    
*/
impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let n: usize = numbers.len();
        let (mut index1, mut index2)= (0, 0);
        let mut found = false;
        for (i, num) in numbers.iter().enumerate(){
            let mut idx: usize = (n-i-1) as usize;

            index1 = idx as i32;
            index2= index1 -1;


            // if numbers[index1 as usize] > target && numbers[index1 as usize] !=0{
            //     continue;
            // }
            
            
            while index2 >= 0 {
                if (numbers[index1 as usize] + numbers[index2 as usize]) == target{
                    found = true;
                    break;                    
                }
                else {
                    index2 -=1;
                }
            }
            if found {break}
            
        }

        return vec![index2+1, index1+1];
    }
}