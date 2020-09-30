/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode a=head;
        if(head==null || head.next ==null){
            return false;
        }
        while(head!=null){
           
            if(head.next==null){return false;}
           
            if(head.next.next==null){return false;}
            if(head.next.next==a){return true;}
            ListNode next=head.next;
             head.next=a;
            head=next;

        }return false;
        
    }
}
