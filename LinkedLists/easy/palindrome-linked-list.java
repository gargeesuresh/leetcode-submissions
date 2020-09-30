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
    public boolean isPalindrome(ListNode head) {
        if(head==null){return true;}
        ListNode f=head,s=head;
        
        while(f.next!=null&&f.next.next!=null){
           f=f.next.next;
            s=s.next;
        }
        if(f.next!=null){
            s=s.next;
        }
        f=head;
        s=rev(s);
        while(s!=null){
            if(s.val!=f.val){return false;}
            f=f.next;
            s=s.next;
        }
        return true;
    
    }
    
    public ListNode rev(ListNode head){
        ListNode prev=null;
        while(head!=null){
            ListNode next=head.next;
            head.next=prev;
            prev=head;
            head=next;
        } return prev;
    }
}
    
