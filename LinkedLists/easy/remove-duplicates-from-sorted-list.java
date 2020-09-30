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
    public ListNode deleteDuplicates(ListNode head) {
       if(head==null || head.next==null)
       {
           return head;
       }
        ListNode ret=head;
        ListNode a=head.next;
        while(a!=null)
        {
            if(a.val==head.val)
            {
                head.next=a.next;
                a=a.next;
            }
            else
            {
                head=head.next;
                a=a.next;
            }
        }
        return ret;
    }
}
