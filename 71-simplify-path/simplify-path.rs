/*
convert into canonical path
multiple slashes = single

invalid things like ... are treated as directories

simplify path

split by /

filter empty

path length is just 3000

save into a stack, if .., pop twice, if ., pop

so if 
...
b
d
./

*/
use std::collections::VecDeque;
impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut q: VecDeque<&str> = VecDeque::new();
        let items: Vec<&str> = path.split('/').collect();
        let mut res: String = String::from('/');
        for item in items {
            if item == ".." as &str {
                q.pop_back();
            }
            else if item != "" as &str && item != "." as &str{
                q.push_back(item);
            }
        }
        for item in q {
            if res.len()  >1{
            res.push_str("/" as &str);

            }
            res.push_str(item);
        }
        return res
    }
}