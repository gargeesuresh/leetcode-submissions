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
    public int getDecimalValue(ListNode head) {
        if(head==null){
            return 0;
        }
        else{
            String t="";
        while(head!=null){
            t+=head.val;
            head=head.next;
        }
            int a=Integer.parseInt(t,2);
            return a;
        }
    }
    }

