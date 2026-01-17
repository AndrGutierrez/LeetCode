use std::collections::HashMap;
use std::collections::hash_map::Entry;
use rand::Rng;
struct RandomizedSet {
    set: HashMap<i32,i32>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {
    fn new() -> Self {
        Self {
            set: HashMap::new(),
        }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        match self.set.entry(val){
            Entry::Occupied(entry)=>{
                return false;
            }
            Entry::Vacant(entry)=>{
                entry.insert(val);
                return true
            }
        }

    }
    
    fn remove(&mut self, val: i32) -> bool {
        match self.set.entry(val){
            Entry::Occupied(entry)=>{
                entry.remove();
                return true;
            }
            Entry::Vacant(entry)=>{
                return false;
            }
        }
    }
    
    fn get_random(&self) -> i32 {
        let mut rng =  rand::thread_rng();
        let vec: Vec<i32> = self.set.clone().into_values().collect();
        let n: i32 = vec.len() as i32;

        let random_number:usize = rng.gen_range(0..n) as usize;
        //println!("{:?}", vec);
        //return 1;
        return vec[random_number];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */