impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut aux: Vec<i32>= nums.iter().filter(|&x| *x!=val).copied().collect();
        let k: i32 = aux.len().try_into().unwrap();
        aux.resize(nums.len(), 0);
        *nums =aux;

        return k;
    }
}