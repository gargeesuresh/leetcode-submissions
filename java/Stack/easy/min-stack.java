class MinStack {

    /** initialize your data structure here. */
    private Node head;
    private class Node{
        int val;
        int min;
        Node Next;
        private Node(int x,int y){
            this.val=x;
            this.min=y;
            this.Next=null;
        }
         private Node(int x,int y,Node n){
            this.val=x;
            this.min=y;
            this.Next=n;
        }
    }
    
    public void push(int x) {
        if(head==null){head=new Node(x,x);}
        else{
            head =new  Node(x, Math.min(x,head.min),head);
        }
    }
    
    public void pop() {
        head=head.Next;
    }
    
    public int top() {
        return head.val;
    }
    
    public int getMin() {
        return head.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
