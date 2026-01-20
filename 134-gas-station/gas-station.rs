impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n: i32 = gas.len() as i32;
        let mut differences: Vec<i32> = Vec::<i32>::new();
        let mut total = 0;
        let mut cycle_completed = false;
        let mut nodes_visited=0;
        for i in 0..n {
            let idx: usize=i as usize;
            let difference = gas[idx]-cost[idx];
            differences.push(difference);
            total+=difference;
        }
    
        if total >=0 {
            let mut i = 0;
            let mut carry = 0;
            while !cycle_completed{
                if i >=n{i=0};
                carry+=differences[i as usize] ;
                if carry <0{
                    nodes_visited=0;
                    carry = 0;
                }
                else{
                    nodes_visited+=1
                }
                if nodes_visited >=n {
                    break;
                }
                i+=1;
            }
            if i+1>=n {return 0}
            return i+1;
        }
        else{
            return -1
        }
    }
}