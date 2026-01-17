use std::collections::HashMap;
use std::collections::hash_map::Entry;
use rand::Rng;

struct RandomizedSet {
    set: HashMap<i32,i32>,
    copy: Vec<i32>

}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {
    fn new() -> Self {
        Self {
            set: HashMap::new(),
            copy: Vec::new()
        }
    }
    
    fn insert(&mut self, val: i32) -> bool {

        match self.set.entry(val){
            Entry::Occupied(entry)=>{
                return false;
            }
            Entry::Vacant(entry)=>{
                self.copy.push(val);
                entry.insert((self.copy.len()-1) as i32);

                return true
            }
        }

    }
    
    fn remove(&mut self, val: i32) -> bool {
        match self.set.entry(val){
            Entry::Occupied(mut entry)=>{
                let latest_element = self.copy[self.copy.len()-1];
                let current_index = *entry.get_mut();
                entry.remove();
                self.copy.swap_remove(current_index as usize);

                if val!=latest_element{
                    self.set.insert(latest_element, current_index);
                }

                return true;
            }
            Entry::Vacant(entry)=>{
                return false;
            }
        }
    }
    
    fn get_random(&self) -> i32 {
        let n: i32 = self.copy.len() as i32;
        let mut random = rand::thread_rng();
        let i: usize= random.gen_range(0..n) as usize;
        return self.copy[i];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */