/*
arrows can burst multiple balloons, but we need to return the minimum number of arrows to burst all balloons

optimization? greedy? 

we need to find which intervals overlap, and for these its just one, for the others one each one

there are much points so it might be O(n), 

try sorted first then make it better, often requires sorting

so, you have a sorted array of intervals


let current = intervals[0]
let i =0
while i < n
    while interval[0] < current[1]:
        i+=1
    i+=1
    current = intervals[i]

    arrows_needed+=1

    thats the number of arrows needed


how do i purpose this as greedy

minimum optimal that stacks to maximum optimal

minimum number of arrows is 1

if the arrow bursts this one
*/

impl Solution {
    pub fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
        if points.len() == 0 {return 0}
        points.sort_by_key(|item| item[1]);
        let aux = points.clone();
        let mut res = 0;
        let mut arrows_needed = 1;
        let mut current = &aux[0];
            
        let mut first_end = aux[0][1];

        for interval in aux {
            let start = interval[0];
            let end = interval[1];
            if first_end < start {
                arrows_needed+=1;
                first_end = end;
            }
                
                
        }
        return arrows_needed;
    }
}