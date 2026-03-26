// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

/*
says head of the merged list so i suppose it doesnt have to be in place

1, 9999
2, 3, 4, 99999

both lists are already sorted

the number of lists both is in the range 0 to 50 so i tihnk i can just convert to array, sort
and make new
*/
impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut items: Vec<i32> = vec![];
        
        let mut head1 = list1;
        let mut head2 = list2;
        while head1.is_some(){
            let aux = head1.clone().unwrap();
            items.push(aux.val);
            head1 = aux.next;
        } 
        while head2.is_some(){
            let aux = head2.clone().unwrap();
            items.push(aux.val);
            head2 = aux.next;
        } 
        items.sort();
        let mut head =  Box::new(ListNode::new(0));
        let mut curr = &mut head;
        for item in items {
            curr.next= Some(Box::new(ListNode::new(item)));
            curr = curr.next.as_mut().unwrap();
        }
        return head.next;
    }
}