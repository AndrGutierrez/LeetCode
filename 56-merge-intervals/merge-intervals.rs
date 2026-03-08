/*
return all not overlapping intervals

is it soreted? no


size of intervals suggest a O(n) solution

sliding window...?

doesnt seem to

if i save the start of each interval and sort it... no

make generalizations:

let interval a
let interval b

let soa start of a
let sob start of b

let eoa = end of a
let eob = end of b

define initial intervals

if soa <= eob and eoa >= sob 

where b > a


brute force?

for inter in intervals
    for inter in intrervals
        check if overlap 

no, on2

if we start with broader intervals...?

save intervals, check if overlaps with any of the other intervals

save into new interval,

repeat until theres no changes

in the end its onlgon
*/
use std::cmp::max;
impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut aux: Vec<Vec<i32>> = intervals.clone();
        aux.sort_by_key(|item| item[0]);
        let mut res: Vec<Vec<i32>> = vec![];
        let mut current: Vec<i32> = aux[0].clone();
        
        for interval in aux {
            let eoa: i32 = current[1];
            let soa: i32 = current[0];

            let eob: i32 =  interval[1];
            let sob: i32 = interval[0];
            if sob <= eoa {
                current = vec![soa, max(eoa, eob)];
            } 
            else {
                res.push(current);
                current = interval;

            }


        }
                res.push(current);

        return res;
    }
}