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
    public ListNode removeElements(ListNode head, int val) {
       if(head==null){return head;}
        
        while(head.val==val && head!=null){
           if(head.next==null){return null;}
            head=head.next;
        }
        ListNode a=head.next;
        ListNode prev=head;
        while(a!=null)
        {
            if(a.val==val)
            {
                if(a.next!=null)
                {
                    prev.next=a.next;
                    a=a.next;
                    
                }
                else
                {
                  prev.next=null;
                    a=null;
                }
            }
            else
            {
              prev=a;
                a=a.next;
            }
        }return head;
    }
}
