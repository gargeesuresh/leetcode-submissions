/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        if(head==null){
            return head;
        }
        else{
            int i=0;
            ListNode a=head;
            while(head!=null){
                head=head.next;
                if(i==1){
                    a=a.next;
                    i=0;
                }
                else{
                   i=1; 
                }
                
            }
            return a;
        }
    }
}
